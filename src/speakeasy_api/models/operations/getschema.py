"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class GetSchemaRequest:
    
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to get the schema for."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to delete metadata for."""
    

@dataclasses.dataclass
class GetSchemaResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""OK"""
    