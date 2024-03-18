# coding: utf-8

"""
    Swagger CrowdSec

    CrowdSec local API

    The version of the OpenAPI document: 1.0.0
    Contact: contact@crowdsec.net
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredErrorResponse(TypedDict):
    # Error message
    message: str

class OptionalErrorResponse(TypedDict, total=False):
    # more detail on individual errors
    errors: str

class ErrorResponse(RequiredErrorResponse, OptionalErrorResponse):
    pass
