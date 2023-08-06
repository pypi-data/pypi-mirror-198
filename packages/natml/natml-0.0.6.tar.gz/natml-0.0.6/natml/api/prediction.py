# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from __future__ import annotations
from base64 import b64encode
from dataclasses import dataclass
from io import BytesIO
from PIL import Image
from typing import Optional, List

from .api import query
from .dtype import Dtype
from .feature import Feature

@dataclass
class FeatureInput:
    """
    Prediction feature input.

    Members:
        name (str): Feature name. This MUST match the input parameter name defined by the predictor endpoint.
        data (str): Feature data URL. This can be a web URL or a data URL.
        type (Dtype): Feature data type.
        shape (list): Feature shape. This MUST be provided for array features.
    """
    name: str
    data: str
    type: Dtype
    shape: Optional[List[int]] = None

@dataclass
class PredictionSession:
    """
    Predictor endpoint session.

    Members:
        id (str): Session ID.
        predictor (Predictor): Predictor for which this session was created.
        created (str): Date created.
        results (list): Prediction results.
        latency (float): Prediction latency in milliseconds.
        error (str): Prediction error. This is `null` if the prediction completed successfully.
        logs (str): Prediction logs.
    """
    id: str
    created: str
    results: List[Feature]
    latency: float
    error: str
    logs: str

    def __post_init__ (self):
        self.results = [Feature(**feature) if isinstance(feature, dict) else feature for feature in self.results]

    @classmethod
    def create (
        cls,
        tag: str,
        *features: List[FeatureInput],
        parse_outputs: bool=True,
        access_key: str=None,
        **inputs,
    ) -> PredictionSession:
        """
        Create an endpoint prediction session.

        Parameters:
            tag (str): Endpoint tag.
            features (list): Input features.
            parse_outputs (bool): Parse output features into Pythonic data types.
            access_key (str): NatML access key.
            inputs (dict): Input features.

        Returns:
            PredictionSession: Prediction session.
        """
        # Collect input features
        input_features = list(features) + [_create_input_feature(key, value) for key, value in inputs.items()]
        parsed_fields = "\n".join(_FEATURE_KEYS) if parse_outputs else ""
        # Query
        response = query(f"""
            mutation ($input: CreatePredictionSessionInput!) {{
                createPredictionSession (input: $input) {{
                    id
                    created
                    results {{
                        data
                        type
                        shape
                        {parsed_fields}
                    }}
                    latency
                    error
                    logs
                }}
            }}""",
            { "tag": tag, "inputs": input_features },
            access_key=access_key
        )
        # Check session
        session = response["createPredictionSession"]
        if not session:
            return None
        # Parse outputs
        session["results"] = [_parse_output_feature(feature) for feature in session["results"]] if session["results"] else None
        session = PredictionSession(**session)
        # Return
        return session
    
def _create_input_feature (key: str, value):
    # Float
    if isinstance(value, float):
        return { "name": key, "floatValue": value }
    # Boolean
    if isinstance(value, bool):
        return { "name": key, "boolValue": value }
    # Integer
    if isinstance(value, int):
        return { "name": key, "intValue": value }
    # String
    if isinstance(value, str):
        return { "name": key, "stringValue": value }
    # Image
    if isinstance(value, Image.Image):
        image_buffer = BytesIO()
        channels = { "L": 1, "RGB": 3, "RGBA": 4 }[value.mode]
        format = "PNG" if value.mode == "RGBA" else "JPEG"
        value.save(image_buffer, format=format)
        encoded_data = b64encode(image_buffer.getvalue()).decode("ascii")
        return {
            "name": key,
            "data": f"data:{value.get_format_mimetype()};base64,{encoded_data}",
            "type": "image",
            "shape": [1, value.height, value.width, channels]
        }
    # Unsupported
    raise RuntimeError(f"Cannot create input feature for value {value} of type {type(value)}")

def _parse_output_feature (feature: dict):
    values = [feature.get(key, None) for key in _FEATURE_KEYS]
    return next((value for value in values if value), feature)

_FEATURE_KEYS = ["stringValue", "floatValue", "floatArray", "intValue", "intArray", "boolValue", "boolArray"]