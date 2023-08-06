from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.poolmanager.v1beta1 import genesis_pb2 as _genesis_pb2
from osmosis.poolmanager.v1beta1 import tx_pb2 as _tx_pb2
from osmosis.poolmanager.v1beta1 import swap_route_pb2 as _swap_route_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EstimateSwapExactAmountInRequest(_message.Message):
    __slots__ = ['pool_id', 'routes', 'sender', 'token_in']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    routes: _containers.RepeatedCompositeFieldContainer[_swap_route_pb2.SwapAmountInRoute]
    sender: str
    token_in: str

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., token_in: _Optional[str]=..., routes: _Optional[_Iterable[_Union[_swap_route_pb2.SwapAmountInRoute, _Mapping]]]=...) -> None:
        ...

class EstimateSwapExactAmountInResponse(_message.Message):
    __slots__ = ['token_out_amount']
    TOKEN_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_out_amount: str

    def __init__(self, token_out_amount: _Optional[str]=...) -> None:
        ...

class EstimateSwapExactAmountOutRequest(_message.Message):
    __slots__ = ['pool_id', 'routes', 'sender', 'token_out']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    routes: _containers.RepeatedCompositeFieldContainer[_swap_route_pb2.SwapAmountOutRoute]
    sender: str
    token_out: str

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., routes: _Optional[_Iterable[_Union[_swap_route_pb2.SwapAmountOutRoute, _Mapping]]]=..., token_out: _Optional[str]=...) -> None:
        ...

class EstimateSwapExactAmountOutResponse(_message.Message):
    __slots__ = ['token_in_amount']
    TOKEN_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_in_amount: str

    def __init__(self, token_in_amount: _Optional[str]=...) -> None:
        ...

class NumPoolsRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class NumPoolsResponse(_message.Message):
    __slots__ = ['num_pools']
    NUM_POOLS_FIELD_NUMBER: _ClassVar[int]
    num_pools: int

    def __init__(self, num_pools: _Optional[int]=...) -> None:
        ...

class ParamsRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class ParamsResponse(_message.Message):
    __slots__ = ['params']
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _genesis_pb2.Params

    def __init__(self, params: _Optional[_Union[_genesis_pb2.Params, _Mapping]]=...) -> None:
        ...