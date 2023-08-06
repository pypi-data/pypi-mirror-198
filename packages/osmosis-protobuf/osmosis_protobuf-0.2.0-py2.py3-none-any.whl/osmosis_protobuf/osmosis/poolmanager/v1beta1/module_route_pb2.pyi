from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
Balancer: PoolType
DESCRIPTOR: _descriptor.FileDescriptor
Stableswap: PoolType

class ModuleRoute(_message.Message):
    __slots__ = ['pool_id', 'pool_type']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    POOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    pool_type: PoolType

    def __init__(self, pool_type: _Optional[_Union[PoolType, str]]=..., pool_id: _Optional[int]=...) -> None:
        ...

class PoolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []