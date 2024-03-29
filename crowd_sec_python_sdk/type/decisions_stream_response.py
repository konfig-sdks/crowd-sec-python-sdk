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

from crowd_sec_python_sdk.type.get_decisions_response import GetDecisionsResponse

class RequiredDecisionsStreamResponse(TypedDict):
    pass

class OptionalDecisionsStreamResponse(TypedDict, total=False):
    new: GetDecisionsResponse

    deleted: GetDecisionsResponse

class DecisionsStreamResponse(RequiredDecisionsStreamResponse, OptionalDecisionsStreamResponse):
    pass
