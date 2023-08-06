from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SwapAmountInRoute(_message.Message):
    __slots__ = ['pool_id', 'token_out_denom']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OUT_DENOM_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    token_out_denom: str

    def __init__(self, pool_id: _Optional[int]=..., token_out_denom: _Optional[str]=...) -> None:
        ...

class SwapAmountOutRoute(_message.Message):
    __slots__ = ['pool_id', 'token_in_denom']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IN_DENOM_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    token_in_denom: str

    def __init__(self, pool_id: _Optional[int]=..., token_in_denom: _Optional[str]=...) -> None:
        ...