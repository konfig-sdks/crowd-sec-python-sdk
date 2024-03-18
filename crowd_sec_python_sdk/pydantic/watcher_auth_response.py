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
from pydantic import BaseModel, Field, RootModel


class WatcherAuthResponse(BaseModel):
    code: typing.Optional[int] = Field(None, alias='code')

    expire: typing.Optional[str] = Field(None, alias='expire')

    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True