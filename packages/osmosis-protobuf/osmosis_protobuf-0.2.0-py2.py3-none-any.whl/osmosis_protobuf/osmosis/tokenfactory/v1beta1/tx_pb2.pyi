from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgBurn(_message.Message):
    __slots__ = ['amount', 'sender']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    sender: str

    def __init__(self, sender: _Optional[str]=..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgBurnResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgChangeAdmin(_message.Message):
    __slots__ = ['denom', 'new_admin', 'sender']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    NEW_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    denom: str
    new_admin: str
    sender: str

    def __init__(self, sender: _Optional[str]=..., denom: _Optional[str]=..., new_admin: _Optional[str]=...) -> None:
        ...

class MsgChangeAdminResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgCreateDenom(_message.Message):
    __slots__ = ['sender', 'subdenom']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SUBDENOM_FIELD_NUMBER: _ClassVar[int]
    sender: str
    subdenom: str

    def __init__(self, sender: _Optional[str]=..., subdenom: _Optional[str]=...) -> None:
        ...

class MsgCreateDenomResponse(_message.Message):
    __slots__ = ['new_token_denom']
    NEW_TOKEN_DENOM_FIELD_NUMBER: _ClassVar[int]
    new_token_denom: str

    def __init__(self, new_token_denom: _Optional[str]=...) -> None:
        ...

class MsgMint(_message.Message):
    __slots__ = ['amount', 'sender']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    amount: _coin_pb2.Coin
    sender: str

    def __init__(self, sender: _Optional[str]=..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgMintResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSetDenomMetadata(_message.Message):
    __slots__ = ['metadata', 'sender']
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    metadata: _bank_pb2.Metadata
    sender: str

    def __init__(self, sender: _Optional[str]=..., metadata: _Optional[_Union[_bank_pb2.Metadata, _Mapping]]=...) -> None:
        ...

class MsgSetDenomMetadataResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...