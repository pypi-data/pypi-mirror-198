from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.protorev.v1beta1 import protorev_pb2 as _protorev_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SetProtoRevAdminAccountProposal(_message.Message):
    __slots__ = ['account', 'description', 'title']
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    account: str
    description: str
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., account: _Optional[str]=...) -> None:
        ...

class SetProtoRevEnabledProposal(_message.Message):
    __slots__ = ['description', 'enabled', 'title']
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    enabled: bool
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., enabled: bool=...) -> None:
        ...