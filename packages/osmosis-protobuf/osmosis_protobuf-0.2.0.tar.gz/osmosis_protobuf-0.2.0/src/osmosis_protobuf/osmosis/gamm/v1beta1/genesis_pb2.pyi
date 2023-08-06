from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['next_pool_number', 'params', 'pools']
    NEXT_POOL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    POOLS_FIELD_NUMBER: _ClassVar[int]
    next_pool_number: int
    params: Params
    pools: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]

    def __init__(self, pools: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., next_pool_number: _Optional[int]=..., params: _Optional[_Union[Params, _Mapping]]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ['pool_creation_fee']
    POOL_CREATION_FEE_FIELD_NUMBER: _ClassVar[int]
    pool_creation_fee: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, pool_creation_fee: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...