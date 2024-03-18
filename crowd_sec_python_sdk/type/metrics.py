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

from crowd_sec_python_sdk.type.metrics_agent_info import MetricsAgentInfo
from crowd_sec_python_sdk.type.metrics_bouncer_info import MetricsBouncerInfo

class RequiredMetrics(TypedDict):
    # the local version of crowdsec/apil
    apil_version: str

    bouncers: typing.List[MetricsBouncerInfo]

    machines: typing.List[MetricsAgentInfo]

class OptionalMetrics(TypedDict, total=False):
    pass

class Metrics(RequiredMetrics, OptionalMetrics):
    pass