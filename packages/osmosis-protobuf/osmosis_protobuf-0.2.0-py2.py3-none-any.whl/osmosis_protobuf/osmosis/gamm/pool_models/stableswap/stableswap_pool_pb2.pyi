from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Pool(_message.Message):
    __slots__ = ['address', 'future_pool_governor', 'id', 'pool_liquidity', 'pool_params', 'scaling_factor_controller', 'scaling_factors', 'total_shares']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POOL_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POOL_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    POOL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SCALING_FACTORS_FIELD_NUMBER: _ClassVar[int]
    SCALING_FACTOR_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARES_FIELD_NUMBER: _ClassVar[int]
    address: str
    future_pool_governor: str
    id: int
    pool_liquidity: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    pool_params: PoolParams
    scaling_factor_controller: str
    scaling_factors: _containers.RepeatedScalarFieldContainer[int]
    total_shares: _coin_pb2.Coin

    def __init__(self, address: _Optional[str]=..., id: _Optional[int]=..., pool_params: _Optional[_Union[PoolParams, _Mapping]]=..., future_pool_governor: _Optional[str]=..., total_shares: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., pool_liquidity: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., scaling_factors: _Optional[_Iterable[int]]=..., scaling_factor_controller: _Optional[str]=...) -> None:
        ...

class PoolParams(_message.Message):
    __slots__ = ['exit_fee', 'swap_fee']
    EXIT_FEE_FIELD_NUMBER: _ClassVar[int]
    SWAP_FEE_FIELD_NUMBER: _ClassVar[int]
    exit_fee: str
    swap_fee: str

    def __init__(self, swap_fee: _Optional[str]=..., exit_fee: _Optional[str]=...) -> None:
        ...