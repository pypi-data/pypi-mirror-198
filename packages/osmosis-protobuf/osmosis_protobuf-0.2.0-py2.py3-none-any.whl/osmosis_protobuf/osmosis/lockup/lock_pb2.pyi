from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
ByDuration: LockQueryType
ByTime: LockQueryType
DESCRIPTOR: _descriptor.FileDescriptor

class PeriodLock(_message.Message):
    __slots__ = ['ID', 'coins', 'duration', 'end_time', 'owner']
    COINS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    duration: _duration_pb2.Duration
    end_time: _timestamp_pb2.Timestamp
    owner: str

    def __init__(self, ID: _Optional[int]=..., owner: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class QueryCondition(_message.Message):
    __slots__ = ['denom', 'duration', 'lock_query_type', 'timestamp']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    LOCK_QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    denom: str
    duration: _duration_pb2.Duration
    lock_query_type: LockQueryType
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, lock_query_type: _Optional[_Union[LockQueryType, str]]=..., denom: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SyntheticLock(_message.Message):
    __slots__ = ['duration', 'end_time', 'synth_denom', 'underlying_lock_id']
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SYNTH_DENOM_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    end_time: _timestamp_pb2.Timestamp
    synth_denom: str
    underlying_lock_id: int

    def __init__(self, underlying_lock_id: _Optional[int]=..., synth_denom: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LockQueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []