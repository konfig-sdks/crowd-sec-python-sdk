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


class Alert(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "scenario_hash",
            "events_count",
            "leakspeed",
            "scenario",
            "simulated",
            "source",
            "message",
            "scenario_version",
            "start_at",
            "events",
            "capacity",
            "stop_at",
        }
        
        class properties:
            scenario = schemas.StrSchema
            scenario_hash = schemas.StrSchema
            scenario_version = schemas.StrSchema
            message = schemas.StrSchema
            events_count = schemas.Int32Schema
            start_at = schemas.StrSchema
            stop_at = schemas.StrSchema
            capacity = schemas.Int32Schema
            leakspeed = schemas.StrSchema
            simulated = schemas.BoolSchema
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Event']:
                        return Event
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Event'], typing.List['Event']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Event':
                    return super().__getitem__(i)
        
            @staticmethod
            def source() -> typing.Type['Source']:
                return Source
            id = schemas.IntSchema
            uuid = schemas.StrSchema
            machine_id = schemas.StrSchema
            created_at = schemas.StrSchema
            remediation = schemas.BoolSchema
            
            
            class decisions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Decision']:
                        return Decision
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Decision'], typing.List['Decision']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'decisions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Decision':
                    return super().__getitem__(i)
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
        
            @staticmethod
            def labels() -> typing.Type['AlertLabels']:
                return AlertLabels
            __annotations__ = {
                "scenario": scenario,
                "scenario_hash": scenario_hash,
                "scenario_version": scenario_version,
                "message": message,
                "events_count": events_count,
                "start_at": start_at,
                "stop_at": stop_at,
                "capacity": capacity,
                "leakspeed": leakspeed,
                "simulated": simulated,
                "events": events,
                "source": source,
                "id": id,
                "uuid": uuid,
                "machine_id": machine_id,
                "created_at": created_at,
                "remediation": remediation,
                "decisions": decisions,
                "meta": meta,
                "labels": labels,
            }
    
    scenario_hash: MetaOapg.properties.scenario_hash
    events_count: MetaOapg.properties.events_count
    leakspeed: MetaOapg.properties.leakspeed
    scenario: MetaOapg.properties.scenario
    simulated: MetaOapg.properties.simulated
    source: 'Source'
    message: MetaOapg.properties.message
    scenario_version: MetaOapg.properties.scenario_version
    start_at: MetaOapg.properties.start_at
    events: MetaOapg.properties.events
    capacity: MetaOapg.properties.capacity
    stop_at: MetaOapg.properties.stop_at
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenario"]) -> MetaOapg.properties.scenario: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenario_hash"]) -> MetaOapg.properties.scenario_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenario_version"]) -> MetaOapg.properties.scenario_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events_count"]) -> MetaOapg.properties.events_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_at"]) -> MetaOapg.properties.start_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_at"]) -> MetaOapg.properties.stop_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leakspeed"]) -> MetaOapg.properties.leakspeed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simulated"]) -> MetaOapg.properties.simulated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'Source': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machine_id"]) -> MetaOapg.properties.machine_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remediation"]) -> MetaOapg.properties.remediation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decisions"]) -> MetaOapg.properties.decisions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> 'AlertLabels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scenario", "scenario_hash", "scenario_version", "message", "events_count", "start_at", "stop_at", "capacity", "leakspeed", "simulated", "events", "source", "id", "uuid", "machine_id", "created_at", "remediation", "decisions", "meta", "labels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenario"]) -> MetaOapg.properties.scenario: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenario_hash"]) -> MetaOapg.properties.scenario_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenario_version"]) -> MetaOapg.properties.scenario_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events_count"]) -> MetaOapg.properties.events_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_at"]) -> MetaOapg.properties.start_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop_at"]) -> MetaOapg.properties.stop_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leakspeed"]) -> MetaOapg.properties.leakspeed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simulated"]) -> MetaOapg.properties.simulated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> 'Source': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machine_id"]) -> typing.Union[MetaOapg.properties.machine_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remediation"]) -> typing.Union[MetaOapg.properties.remediation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decisions"]) -> typing.Union[MetaOapg.properties.decisions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union['AlertLabels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scenario", "scenario_hash", "scenario_version", "message", "events_count", "start_at", "stop_at", "capacity", "leakspeed", "simulated", "events", "source", "id", "uuid", "machine_id", "created_at", "remediation", "decisions", "meta", "labels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scenario_hash: typing.Union[MetaOapg.properties.scenario_hash, str, ],
        events_count: typing.Union[MetaOapg.properties.events_count, decimal.Decimal, int, ],
        leakspeed: typing.Union[MetaOapg.properties.leakspeed, str, ],
        scenario: typing.Union[MetaOapg.properties.scenario, str, ],
        simulated: typing.Union[MetaOapg.properties.simulated, bool, ],
        source: 'Source',
        message: typing.Union[MetaOapg.properties.message, str, ],
        scenario_version: typing.Union[MetaOapg.properties.scenario_version, str, ],
        start_at: typing.Union[MetaOapg.properties.start_at, str, ],
        events: typing.Union[MetaOapg.properties.events, list, tuple, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, ],
        stop_at: typing.Union[MetaOapg.properties.stop_at, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        machine_id: typing.Union[MetaOapg.properties.machine_id, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        remediation: typing.Union[MetaOapg.properties.remediation, bool, schemas.Unset] = schemas.unset,
        decisions: typing.Union[MetaOapg.properties.decisions, list, tuple, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        labels: typing.Union['AlertLabels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Alert':
        return super().__new__(
            cls,
            *args,
            scenario_hash=scenario_hash,
            events_count=events_count,
            leakspeed=leakspeed,
            scenario=scenario,
            simulated=simulated,
            source=source,
            message=message,
            scenario_version=scenario_version,
            start_at=start_at,
            events=events,
            capacity=capacity,
            stop_at=stop_at,
            id=id,
            uuid=uuid,
            machine_id=machine_id,
            created_at=created_at,
            remediation=remediation,
            decisions=decisions,
            meta=meta,
            labels=labels,
            _configuration=_configuration,
            **kwargs,
        )

from crowd_sec_python_sdk.model.alert_labels import AlertLabels
from crowd_sec_python_sdk.model.decision import Decision
from crowd_sec_python_sdk.model.event import Event
from crowd_sec_python_sdk.model.meta import Meta
from crowd_sec_python_sdk.model.source import Source