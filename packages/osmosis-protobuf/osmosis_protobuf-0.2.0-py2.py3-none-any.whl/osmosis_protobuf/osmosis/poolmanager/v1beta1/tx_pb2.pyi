from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.poolmanager.v1beta1 import swap_route_pb2 as _swap_route_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgSwapExactAmountIn(_message.Message):
    __slots__ = ['routes', 'sender', 'token_in', 'token_out_min_amount']
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_swap_route_pb2.SwapAmountInRoute]
    sender: str
    token_in: _coin_pb2.Coin
    token_out_min_amount: str

    def __init__(self, sender: _Optional[str]=..., routes: _Optional[_Iterable[_Union[_swap_route_pb2.SwapAmountInRoute, _Mapping]]]=..., token_in: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., token_out_min_amount: _Optional[str]=...) -> None:
        ...

class MsgSwapExactAmountInResponse(_message.Message):
    __slots__ = ['token_out_amount']
    TOKEN_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_out_amount: str

    def __init__(self, token_out_amount: _Optional[str]=...) -> None:
        ...

class MsgSwapExactAmountOut(_message.Message):
    __slots__ = ['routes', 'sender', 'token_in_max_amount', 'token_out']
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_MAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_swap_route_pb2.SwapAmountOutRoute]
    sender: str
    token_in_max_amount: str
    token_out: _coin_pb2.Coin

    def __init__(self, sender: _Optional[str]=..., routes: _Optional[_Iterable[_Union[_swap_route_pb2.SwapAmountOutRoute, _Mapping]]]=..., token_in_max_amount: _Optional[str]=..., token_out: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgSwapExactAmountOutResponse(_message.Message):
    __slots__ = ['token_in_amount']
    TOKEN_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_in_amount: str

    def __init__(self, token_in_amount: _Optional[str]=...) -> None:
        ...