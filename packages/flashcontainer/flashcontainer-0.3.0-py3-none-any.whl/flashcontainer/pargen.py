"""Pargen main function
"""

# BSD 3-Clause License
#
# Copyright (c) 2022-2023, Haju Schulz (haju.schulz@online.de)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import datetime
import argparse
import logging
import uuid
import sys
import os
from enum import Enum
from pathlib import Path
from typing import List

from flashcontainer.hexwriter import HexWriter
from flashcontainer.xmlparser import XmlParser
from flashcontainer.cfilewriter import CFileWriter
from flashcontainer.gnuldwriter import GnuLdWriter
from flashcontainer.pyhexdumpwriter import PyHexDumpWriter
from flashcontainer.a2lwriter import A2lWriter
from flashcontainer.packageinfo import __version__, __email__, __repository__
import flashcontainer.datamodel as DM

# List of output writers
_WRITER = [
    {
        "key": "ihex",
        "class": HexWriter,
        "help": "Generate intelhex file"
    },
    {
        "key": "csrc",
        "class": CFileWriter,
        "help": "Generate c/c++ header and source files"
    },
    {
        "key": "gld",
        "class": GnuLdWriter,
        "help": "Generate GNU linker include file for parameter symbol generation."
    },
    {
        "key": "a2l",
        "class": A2lWriter,
        "help": "Generate A2L parameter description file."
    },
    {
        "key": "pyhexdump",
        "class": PyHexDumpWriter,
        "help": "Generate pyHexDump print configuration file."
    }
]

def pargen_cli() -> int:
    """ cmd line interface for pagen"""

    logging.basicConfig(encoding='utf-8', level=logging.WARN)

    about = 'A tool for generating flashable parameter container.'
    name = "pargen"

    parser = argparse.ArgumentParser(
        prog=name,
        description=about,
        epilog=f"Visit {__repository__} for full documentation and examples.")

    for writer in _WRITER:
        parser.add_argument("--" + writer["key"], action='store_true', help=writer["help"])

    parser.add_argument(
        '--destdir', '-o', nargs=1,
        help='Specify output directory for generated files', default=[str(Path.cwd())])
    parser.add_argument(
        '--filename', '-f', nargs=1,
        help='Set basename for generated files.')

    parser.add_argument(
        "--static", "-s", action='store_true',
        help='Create static comment output without dynamic elements like date and time.'
    )

    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    parser.add_argument('file', nargs=1, help='XML parameter definition file')

    args = parser.parse_args()

    print(f"{name} {__version__}: {about}")
    print(f"Copyright (c) 2023 {__email__}\n")

    writers = []

    for writer in _WRITER:
        if getattr(args, writer["key"]):
            writers.append(writer["class"])

    return pargen(
        cfgfile=args.file[0],
        filename=args.filename,
        outdir=Path(args.destdir[0]),
        static=args.static,
        writers=writers)

class Error(Enum):
    """Pargen error codes """

    ERROR_OK = 0
    ERROR_FILE_NOT_FOUND = 1
    ERROR_INVALID_FORMAT = 2
    ERROR_VALIDATION_FAIL = 3
    ERROR_EXCEPTION = 4

def pargen(
        cfgfile: str,
        filename: str,
        outdir: Path,
        static: bool,
        writers: List[DM.Walker]) -> int:
    """ Parameter generator tool entry point"""

    # Create output directory (if necessary)
    destdir = Path.resolve(outdir)
    destdir.mkdir(parents=True, exist_ok=True)

    outfilename = filename
    if outfilename is None:
        outfilename = os.path.basename(cfgfile)
    outfilename = Path(outfilename).stem

    if Path(cfgfile).is_file():
        model = XmlParser.from_file(cfgfile)
    else:
        logging.error("file not found: %s", cfgfile)
        return Error.ERROR_FILE_NOT_FOUND.value

    if model is None:
        return Error.ERROR_INVALID_FORMAT.value

    # writer context options
    param = {
        "PNAME": "pargen",
        "VERSION": __version__,
        "INPUT": cfgfile,
        "GUID": uuid.uuid4(),
        "CMDLINE": ' '.join(sys.argv[0:]),
        "DATETIME": datetime.datetime.now(),
        "MODEL": model,
        "DESTDIR": destdir,
        "BASENAME": outfilename,
        "STATICOUTPUT": static
        }

    if model.validate(param) is False:
        return Error.ERROR_VALIDATION_FAIL.value

    if 0 == len(writers):
        logging.warning("no writers defined, generating nothing.")
        return 0

    for writer in writers:
        writer(model, param).run()

    print("Done.")
    return Error.ERROR_OK.value


if __name__ == "__main__":
    try:
        sys.exit(pargen_cli())
    except Exception as exc:  # pylint: disable=broad-except
        logging.exception(exc)
        sys.exit(Error.ERROR_EXCEPTION.value)
