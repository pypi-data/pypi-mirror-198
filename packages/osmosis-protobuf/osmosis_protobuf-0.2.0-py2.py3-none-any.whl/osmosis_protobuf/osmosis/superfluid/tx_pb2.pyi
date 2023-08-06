from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.superfluid import superfluid_pb2 as _superfluid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgLockAndSuperfluidDelegate(_message.Message):
    __slots__ = ['coins', 'sender', 'val_addr']
    COINS_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    VAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    sender: str
    val_addr: str

    def __init__(self, sender: _Optional[str]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., val_addr: _Optional[str]=...) -> None:
        ...

class MsgLockAndSuperfluidDelegateResponse(_message.Message):
    __slots__ = ['ID']
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]

    def __init__(self, ID: _Optional[int]=...) -> None:
        ...

class MsgSuperfluidDelegate(_message.Message):
    __slots__ = ['lock_id', 'sender', 'val_addr']
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    VAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    lock_id: int
    sender: str
    val_addr: str

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=..., val_addr: _Optional[str]=...) -> None:
        ...

class MsgSuperfluidDelegateResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSuperfluidUnbondLock(_message.Message):
    __slots__ = ['lock_id', 'sender']
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    lock_id: int
    sender: str

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=...) -> None:
        ...

class MsgSuperfluidUnbondLockResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSuperfluidUndelegate(_message.Message):
    __slots__ = ['lock_id', 'sender']
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    lock_id: int
    sender: str

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=...) -> None:
        ...

class MsgSuperfluidUndelegateAndUnbondLock(_message.Message):
    __slots__ = ['coin', 'lock_id', 'sender']
    COIN_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    coin: _coin_pb2.Coin
    lock_id: int
    sender: str

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=..., coin: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgSuperfluidUndelegateAndUnbondLockResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSuperfluidUndelegateResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgUnPoolWhitelistedPool(_message.Message):
    __slots__ = ['pool_id', 'sender']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    sender: str

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=...) -> None:
        ...

class MsgUnPoolWhitelistedPoolResponse(_message.Message):
    __slots__ = ['exited_lock_ids']
    EXITED_LOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    exited_lock_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, exited_lock_ids: _Optional[_Iterable[int]]=...) -> None:
        ...