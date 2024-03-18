# coding: utf-8

"""
    Swagger CrowdSec

    CrowdSec local API

    The version of the OpenAPI document: 1.0.0
    Contact: contact@crowdsec.net
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from crowd_sec_python_sdk import schemas  # noqa: F401


class ErrorResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    error response return by the API
    """


    class MetaOapg:
        required = {
            "message",
        }
        
        class properties:
            message = schemas.StrSchema
            errors = schemas.StrSchema
            __annotations__ = {
                "message": message,
                "errors": errors,
            }
    
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        errors: typing.Union[MetaOapg.properties.errors, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ErrorResponse':
        return super().__new__(
            cls,
            *args,
            message=message,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )
