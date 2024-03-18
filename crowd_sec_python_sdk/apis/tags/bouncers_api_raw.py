# coding: utf-8

"""
    Swagger CrowdSec

    CrowdSec local API

    The version of the OpenAPI document: 1.0.0
    Contact: contact@crowdsec.net
    Generated by: https://konfigthis.com
"""

from crowd_sec_python_sdk.paths.decisions_stream.get import GetDecisionsStreamRaw
from crowd_sec_python_sdk.paths.decisions_stream.head import GetDecisionsStream0Raw
from crowd_sec_python_sdk.paths.decisions.get import GetInformationRaw
from crowd_sec_python_sdk.paths.decisions.head import GetInformation0Raw


class BouncersApiRaw(
    GetDecisionsStreamRaw,
    GetDecisionsStream0Raw,
    GetInformationRaw,
    GetInformation0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass