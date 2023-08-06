from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.superfluid import superfluid_pb2 as _superfluid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RemoveSuperfluidAssetsProposal(_message.Message):
    __slots__ = ['description', 'superfluid_asset_denoms', 'title']
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPERFLUID_ASSET_DENOMS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    superfluid_asset_denoms: _containers.RepeatedScalarFieldContainer[str]
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., superfluid_asset_denoms: _Optional[_Iterable[str]]=...) -> None:
        ...

class SetSuperfluidAssetsProposal(_message.Message):
    __slots__ = ['assets', 'description', 'title']
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_superfluid_pb2.SuperfluidAsset]
    description: str
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., assets: _Optional[_Iterable[_Union[_superfluid_pb2.SuperfluidAsset, _Mapping]]]=...) -> None:
        ...

class UpdateUnpoolWhiteListProposal(_message.Message):
    __slots__ = ['description', 'ids', 'is_overwrite', 'title']
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    IS_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    ids: _containers.RepeatedScalarFieldContainer[int]
    is_overwrite: bool
    title: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., ids: _Optional[_Iterable[int]]=..., is_overwrite: bool=...) -> None:
        ...