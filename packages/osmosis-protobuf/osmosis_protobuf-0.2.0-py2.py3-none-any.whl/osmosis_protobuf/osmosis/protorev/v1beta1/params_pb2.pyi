from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['admin', 'enabled']
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    admin: str
    enabled: bool

    def __init__(self, enabled: bool=..., admin: _Optional[str]=...) -> None:
        ...