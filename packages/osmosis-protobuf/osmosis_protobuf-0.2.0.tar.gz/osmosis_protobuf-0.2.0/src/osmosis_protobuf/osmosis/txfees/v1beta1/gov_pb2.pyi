from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.txfees.v1beta1 import feetoken_pb2 as _feetoken_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateFeeTokenProposal(_message.Message):
    __slots__ = ['description', 'feetoken', 'title']
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEETOKEN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    feetoken: _feetoken_pb2.FeeToken
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., feetoken: _Optional[_Union[_feetoken_pb2.FeeToken, _Mapping]]=...) -> None:
        ...