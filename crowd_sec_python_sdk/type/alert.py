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

from crowd_sec_python_sdk.type.alert_labels import AlertLabels
from crowd_sec_python_sdk.type.decision import Decision
from crowd_sec_python_sdk.type.event import Event
from crowd_sec_python_sdk.type.meta import Meta
from crowd_sec_python_sdk.type.source import Source

class RequiredAlert(TypedDict):
    scenario: str

    scenario_hash: str

    scenario_version: str

    # a human readable message
    message: str

    events_count: int

    start_at: str

    stop_at: str

    capacity: int

    leakspeed: str

    simulated: bool

    # the Meta of the events leading to overflow
    events: typing.List[Event]

    source: Source

class OptionalAlert(TypedDict, total=False):
    # only relevant for GET, ignored in POST requests
    id: int

    # only relevant for LAPI->CAPI, ignored for cscli->LAPI and crowdsec->LAPI
    uuid: str

    # only relevant for LAPI->CAPI, ignored for cscli->LAPI and crowdsec->LAPI
    machine_id: str

    # only relevant for GET, ignored in POST requests
    created_at: str

    remediation: bool

    decisions: typing.List[Decision]

    meta: Meta

    labels: AlertLabels

class Alert(RequiredAlert, OptionalAlert):
    pass