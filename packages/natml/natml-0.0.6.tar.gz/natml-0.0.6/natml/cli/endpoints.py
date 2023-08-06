# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from dataclasses import asdict
from pathlib import Path
from rich import print_json
from typer import Argument, Option, Typer

from .auth import get_access_key
from ..api import Endpoint, EndpointType, EndpointAcceleration

app = Typer(no_args_is_help=True)

@app.command(name="retrieve", help="Retrieve a predictor endpoint.")
def retrieve_endpoint (
    tag: str=Argument(..., help="Endpoint tag. If the tag does not contain a variant then the variant defaults to `main`.")
) -> None:
    endpoint = Endpoint.retrieve(tag, access_key=get_access_key())
    endpoint = asdict(endpoint) if endpoint else None
    print_json(data=endpoint)

@app.command(name="list", help="List all predictor endpoints.")
def list_endpoints (
    tag: str=Argument(..., help="Predictor tag. This MUST NOT be a variant tag.")
) -> None:
    endpoints = Endpoint.list(tag, access_key=get_access_key())
    endpoints = [asdict(endpoint) for endpoint in endpoints] if endpoints else None
    print_json(data=endpoints)

@app.command(name="create", help="Create a predictor endpoint.")
def create_endpoint (
    tag: str=Argument(..., help="Predictor tag."),
    notebook: Path=Argument(..., help="Path to endpoint notebook."),
    type: EndpointType=Option(EndpointType.Serverless, case_sensitive=False, help="Endpoint type."),
    acceleration: EndpointAcceleration=Option(EndpointAcceleration.CPU, case_sensitive=False, help="Endpoint acceleration."),
) -> None:
    endpoint = Endpoint.create(tag, notebook, type, acceleration, access_key=get_access_key())
    endpoint = asdict(endpoint)
    print_json(data=endpoint)

@app.command(name="delete", help="Delete a predictor endpoint.")
def delete_endpoint (
    tag: str=Argument(..., help="Predictor tag.")
) -> None:
    result = Endpoint.delete(tag, access_key=get_access_key())
    print_json(data=result)