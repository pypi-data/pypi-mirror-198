from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.poolmanager.v1beta1 import swap_route_pb2 as _swap_route_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgExitPool(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_in_amount', 'token_out_mins']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_MINS_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_in_amount: str
    token_out_mins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., share_in_amount: _Optional[str]=..., token_out_mins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgExitPoolResponse(_message.Message):
    __slots__ = ['token_out']
    TOKEN_OUT_FIELD_NUMBER: _ClassVar[int]
    token_out: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, token_out: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgExitSwapExternAmountOut(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_in_max_amount', 'token_out']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_IN_MAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_in_max_amount: str
    token_out: _coin_pb2.Coin

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., token_out: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., share_in_max_amount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapExternAmountOutResponse(_message.Message):
    __slots__ = ['share_in_amount']
    SHARE_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    share_in_amount: str

    def __init__(self, share_in_amount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapShareAmountIn(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_in_amount', 'token_out_denom', 'token_out_min_amount']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_DENOM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_in_amount: str
    token_out_denom: str
    token_out_min_amount: str

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., token_out_denom: _Optional[str]=..., share_in_amount: _Optional[str]=..., token_out_min_amount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapShareAmountInResponse(_message.Message):
    __slots__ = ['token_out_amount']
    TOKEN_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_out_amount: str

    def __init__(self, token_out_amount: _Optional[str]=...) -> None:
        ...

class MsgJoinPool(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_out_amount', 'token_in_maxs']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_MAXS_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_out_amount: str
    token_in_maxs: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., share_out_amount: _Optional[str]=..., token_in_maxs: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgJoinPoolResponse(_message.Message):
    __slots__ = ['share_out_amount', 'token_in']
    SHARE_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_FIELD_NUMBER: _ClassVar[int]
    share_out_amount: str
    token_in: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, share_out_amount: _Optional[str]=..., token_in: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgJoinSwapExternAmountIn(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_out_min_amount', 'token_in']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_OUT_MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_out_min_amount: str
    token_in: _coin_pb2.Coin

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., token_in: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., share_out_min_amount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapExternAmountInResponse(_message.Message):
    __slots__ = ['share_out_amount']
    SHARE_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    share_out_amount: str

    def __init__(self, share_out_amount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapShareAmountOut(_message.Message):
    __slots__ = ['pool_id', 'sender', 'share_out_amount', 'token_in_denom', 'token_in_max_amount']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SHARE_OUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_DENOM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_MAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str
    share_out_amount: str
    token_in_denom: str
    token_in_max_amount: str

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=..., token_in_denom: _Optional[str]=..., share_out_amount: _Optional[str]=..., token_in_max_amount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapShareAmountOutResponse(_message.Message):
    __slots__ = ['token_in_amount']
    TOKEN_IN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_in_amount: str

    def __init__(self, token_in_amount: _Optional[str]=...) -> None:
        ...

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