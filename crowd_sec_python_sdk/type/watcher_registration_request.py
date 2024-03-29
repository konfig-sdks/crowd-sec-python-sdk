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


class RequiredWatcherRegistrationRequest(TypedDict):
    machine_id: str

    password: str

class OptionalWatcherRegistrationRequest(TypedDict, total=False):
    pass

class WatcherRegistrationRequest(RequiredWatcherRegistrationRequest, OptionalWatcherRegistrationRequest):
    pass
