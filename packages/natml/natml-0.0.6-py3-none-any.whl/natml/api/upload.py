# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from enum import Enum
from mimetypes import guess_type
from pathlib import Path
from requests import put

from .api import query

class UploadType (str, Enum):
    """
    Upload URL type.
    """
    Demo = "DEMO"
    Feature = "FEATURE"
    Graph = "GRAPH"
    Media = "MEDIA"
    Notebook = "NOTEBOOK"

def create_upload_url (type: UploadType, name: str, key: str=None) -> str:
    """
    Create an upload URL.

    Parameters:
        type (UploadType): Upload type.
        name (str): File name.
        key (str): File key. This is useful for grouping related files.

    Returns:
        str: File upload URL.
    """
    response = query(f"""
        mutation ($input: CreateUploadURLInput!) {{
            createUploadURL (input: $input)
        }}
        """,
        { "type": type, "name": name, "key": key }
    )
    url = response["createUploadURL"]
    return url

def upload_file (path: Path, type: UploadType, key: str=None, check_extension: bool=True) -> str:
    """
    Upload a file and return the URL.

    Parameters:
        path (Path): File path.
        type (UploadType): File type.
        key (str): File key. This is useful for grouping related files.
        check_extension (bool): Validate file extensions before uploading.

    Returns:
        str: Upload URL.
    """
    EXTENSIONS = {
        UploadType.Demo: [".data", ".js"],
        UploadType.Feature: [],
        UploadType.Graph: [".mlmodel", ".onnx", ".tflite"],
        UploadType.Media: [".jpg", ".jpeg", ".png", ".gif"],
        UploadType.Notebook: [".ipynb"],
    }
    # Check path
    if not path.exists():
        raise RuntimeError(f"Cannot upload {path.name} because the file does not exist")
    # Check file
    if not path.is_file():
        raise RuntimeError(f"Cannot upload {path.name} becaause it does not point to a file")
    # Check extension
    if check_extension and path.suffix not in EXTENSIONS[type]:
        raise RuntimeError(f"Cannot upload {path.name} because it is not a valid {type.name.lower()} file")
    # Get upload URL
    mime = guess_type(path, strict=False)[0] or "application/binary"
    url = create_upload_url(type, path.name, key=key)
    with open(path, "rb") as f:
        put(url, data=f, headers={ "Content-Type": mime }).raise_for_status()
    # Return
    return url