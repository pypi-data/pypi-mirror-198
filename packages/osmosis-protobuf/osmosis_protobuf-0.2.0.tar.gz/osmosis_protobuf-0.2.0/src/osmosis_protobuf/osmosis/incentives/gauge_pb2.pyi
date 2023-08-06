from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.lockup import lock_pb2 as _lock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Gauge(_message.Message):
    __slots__ = ['coins', 'distribute_to', 'distributed_coins', 'filled_epochs', 'id', 'is_perpetual', 'num_epochs_paid_over', 'start_time']
    COINS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTED_COINS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTE_TO_FIELD_NUMBER: _ClassVar[int]
    FILLED_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_PERPETUAL_FIELD_NUMBER: _ClassVar[int]
    NUM_EPOCHS_PAID_OVER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    distribute_to: _lock_pb2.QueryCondition
    distributed_coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    filled_epochs: int
    id: int
    is_perpetual: bool
    num_epochs_paid_over: int
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., is_perpetual: bool=..., distribute_to: _Optional[_Union[_lock_pb2.QueryCondition, _Mapping]]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., num_epochs_paid_over: _Optional[int]=..., filled_epochs: _Optional[int]=..., distributed_coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class LockableDurationsInfo(_message.Message):
    __slots__ = ['lockable_durations']
    LOCKABLE_DURATIONS_FIELD_NUMBER: _ClassVar[int]
    lockable_durations: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]

    def __init__(self, lockable_durations: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=...) -> None:
        ...