# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from dataclasses import asdict
from pathlib import Path
from rich import print_json
from typer import Argument, Typer

from .auth import get_access_key
from ..api import Graph, GraphFormat, PredictorSession

app = Typer(no_args_is_help=True)

@app.command(name="retrieve", help="Retrieve a predictor graph.")
def retrieve_graph (
    tag: str=Argument(..., help="Graph tag. If the tag does not contain a variant then the variant defaults to `main`."),
    format: GraphFormat=Argument(..., case_sensitive=False, help="Graph format.")
) -> None:
    graph = Graph.retrieve(tag, format, access_key=get_access_key())
    graph = asdict(graph) if graph else None
    print_json(data=graph)

@app.command(name="list", help="List all predictor graphs.")
def list_graph (
    tag: str=Argument(..., help="Predictor tag. This MUST NOT be a variant tag.")
) -> None:
    graphs = Graph.list(tag, access_key=get_access_key())
    graphs = [asdict(graph) for graph in graphs] if graphs else None
    print_json(data=graphs)

@app.command(name="create", help="Create a predictor graph.")
def create_graph (
    tag: str=Argument(..., help="Graph tag. If the tag does not contain a variant then the variant defaults to `main`."),
    graph: Path=Argument(..., help="Path to ML graph."),
    format: GraphFormat=Argument(..., case_sensitive=False, help="Target graph format.")
) -> None:
    graph = Graph.create(tag, graph, format, access_key=get_access_key())
    graph = asdict(graph)
    print_json(data=graph)

@app.command(name="delete", help="Delete a predictor graph.")
def delete_graph (
    tag: str=Argument(..., help="Graph tag. If the tag does not contain a variant then the variant defaults to `main`."),
    format: GraphFormat=Argument(..., case_sensitive=False, help="Graph format.")
) -> None:
    result = Graph.delete(tag, format, access_key=get_access_key())
    print_json(data=result)

@app.command(name="predict", help="Create a graph prediction session.")
def create_predictor_session (
    tag: str=Argument(..., help="Graph tag. If the tag does not contain a variant then the variant defaults to `main`."),
    format: GraphFormat=Argument(..., case_sensitive=False, help="Graph format.")
) -> None:
    session = PredictorSession.create(tag, format, access_key=get_access_key())
    session = asdict(session)
    print_json(data=session)