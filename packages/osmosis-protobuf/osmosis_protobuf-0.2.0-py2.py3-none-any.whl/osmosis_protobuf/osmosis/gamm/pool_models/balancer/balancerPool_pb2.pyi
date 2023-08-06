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
    __slots__ = ['address', 'future_pool_governor', 'id', 'pool_assets', 'pool_params', 'total_shares', 'total_weight']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POOL_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POOL_ASSETS_FIELD_NUMBER: _ClassVar[int]
    POOL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    address: str
    future_pool_governor: str
    id: int
    pool_assets: _containers.RepeatedCompositeFieldContainer[PoolAsset]
    pool_params: PoolParams
    total_shares: _coin_pb2.Coin
    total_weight: str

    def __init__(self, address: _Optional[str]=..., id: _Optional[int]=..., pool_params: _Optional[_Union[PoolParams, _Mapping]]=..., future_pool_governor: _Optional[str]=..., total_shares: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., pool_assets: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=..., total_weight: _Optional[str]=...) -> None:
        ...

class PoolAsset(_message.Message):
    __slots__ = ['token', 'weight']
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    token: _coin_pb2.Coin
    weight: str

    def __init__(self, token: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., weight: _Optional[str]=...) -> None:
        ...

class PoolParams(_message.Message):
    __slots__ = ['exit_fee', 'smooth_weight_change_params', 'swap_fee']
    EXIT_FEE_FIELD_NUMBER: _ClassVar[int]
    SMOOTH_WEIGHT_CHANGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SWAP_FEE_FIELD_NUMBER: _ClassVar[int]
    exit_fee: str
    smooth_weight_change_params: SmoothWeightChangeParams
    swap_fee: str

    def __init__(self, swap_fee: _Optional[str]=..., exit_fee: _Optional[str]=..., smooth_weight_change_params: _Optional[_Union[SmoothWeightChangeParams, _Mapping]]=...) -> None:
        ...

class SmoothWeightChangeParams(_message.Message):
    __slots__ = ['duration', 'initial_pool_weights', 'start_time', 'target_pool_weights']
    DURATION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_POOL_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_POOL_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    initial_pool_weights: _containers.RepeatedCompositeFieldContainer[PoolAsset]
    start_time: _timestamp_pb2.Timestamp
    target_pool_weights: _containers.RepeatedCompositeFieldContainer[PoolAsset]

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., initial_pool_weights: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=..., target_pool_weights: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=...) -> None:
        ...