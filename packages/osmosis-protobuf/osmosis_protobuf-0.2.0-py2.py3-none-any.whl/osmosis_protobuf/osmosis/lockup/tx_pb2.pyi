from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.lockup import lock_pb2 as _lock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgBeginUnlocking(_message.Message):
    __slots__ = ['ID', 'coins', 'owner']
    COINS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    owner: str

    def __init__(self, owner: _Optional[str]=..., ID: _Optional[int]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgBeginUnlockingAll(_message.Message):
    __slots__ = ['owner']
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: str

    def __init__(self, owner: _Optional[str]=...) -> None:
        ...

class MsgBeginUnlockingAllResponse(_message.Message):
    __slots__ = ['unlocks']
    UNLOCKS_FIELD_NUMBER: _ClassVar[int]
    unlocks: _containers.RepeatedCompositeFieldContainer[_lock_pb2.PeriodLock]

    def __init__(self, unlocks: _Optional[_Iterable[_Union[_lock_pb2.PeriodLock, _Mapping]]]=...) -> None:
        ...

class MsgBeginUnlockingResponse(_message.Message):
    __slots__ = ['success', 'unlockingLockID']
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    UNLOCKINGLOCKID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    unlockingLockID: int

    def __init__(self, success: bool=..., unlockingLockID: _Optional[int]=...) -> None:
        ...

class MsgExtendLockup(_message.Message):
    __slots__ = ['ID', 'duration', 'owner']
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    owner: str

    def __init__(self, owner: _Optional[str]=..., ID: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class MsgExtendLockupResponse(_message.Message):
    __slots__ = ['success']
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class MsgForceUnlock(_message.Message):
    __slots__ = ['ID', 'coins', 'owner']
    COINS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    owner: str

    def __init__(self, owner: _Optional[str]=..., ID: _Optional[int]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgForceUnlockResponse(_message.Message):
    __slots__ = ['success']
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class MsgLockTokens(_message.Message):
    __slots__ = ['coins', 'duration', 'owner']
    COINS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    duration: _duration_pb2.Duration
    owner: str

    def __init__(self, owner: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgLockTokensResponse(_message.Message):
    __slots__ = ['ID']
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]

    def __init__(self, ID: _Optional[int]=...) -> None:
        ...