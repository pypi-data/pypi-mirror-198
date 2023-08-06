# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from dataclasses import asdict
from pathlib import Path
from rich import print_json
from typer import Argument, Context, Option

from .auth import get_access_key
from ..api import PredictionSession

def predict (
    tag: str = Argument(..., help="Predictor tag."),
    raw_outputs: bool = Option(False, "--raw-outputs", help="Generate raw output features instead of parsing."),
    context: Context = 0
) -> None:
    inputs = { context.args[i].replace("-", ""): _parse_value(context.args[i+1]) for i in range(0, len(context.args), 2) }
    session = PredictionSession.create(tag, **inputs, parse_outputs=not raw_outputs, access_key=get_access_key())
    print_json(data=asdict(session))

def _parse_value (value: str):
    """
    Parse a value from a CLI argument.

    Parameters:
        value (str): CLI input argument.

    Returns:
        bool | int | float | str | Path: Parsed value.
    """
    # Boolean
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    # Integer
    try:
        return int(value)
    except ValueError:
        pass
    # Float
    try:
        return float(value)
    except ValueError:
        pass
    # File
    if value.startswith("@"):
        return Path(value[1:])
    # String
    return value