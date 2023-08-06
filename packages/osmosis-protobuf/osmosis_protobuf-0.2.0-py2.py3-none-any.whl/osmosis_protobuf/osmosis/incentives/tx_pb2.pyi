from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.incentives import gauge_pb2 as _gauge_pb2
from osmosis.lockup import lock_pb2 as _lock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgAddToGauge(_message.Message):
    __slots__ = ['gauge_id', 'owner', 'rewards']
    GAUGE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    gauge_id: int
    owner: str
    rewards: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, owner: _Optional[str]=..., gauge_id: _Optional[int]=..., rewards: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgAddToGaugeResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgCreateGauge(_message.Message):
    __slots__ = ['coins', 'distribute_to', 'is_perpetual', 'num_epochs_paid_over', 'owner', 'start_time']
    COINS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTE_TO_FIELD_NUMBER: _ClassVar[int]
    IS_PERPETUAL_FIELD_NUMBER: _ClassVar[int]
    NUM_EPOCHS_PAID_OVER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    distribute_to: _lock_pb2.QueryCondition
    is_perpetual: bool
    num_epochs_paid_over: int
    owner: str
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, is_perpetual: bool=..., owner: _Optional[str]=..., distribute_to: _Optional[_Union[_lock_pb2.QueryCondition, _Mapping]]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., num_epochs_paid_over: _Optional[int]=...) -> None:
        ...

class MsgCreateGaugeResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...