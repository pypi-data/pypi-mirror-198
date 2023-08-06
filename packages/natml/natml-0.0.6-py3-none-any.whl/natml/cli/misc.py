# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from rich import print
from typer import Exit, Option

from ..version import __version__

def _version_callback (value: bool):
    if value:
        print(__version__)
        raise Exit()

def main_cli_options (
    version: bool = Option(None, "--version", callback=_version_callback, help="Get the NatML CLI version.")
):
    pass