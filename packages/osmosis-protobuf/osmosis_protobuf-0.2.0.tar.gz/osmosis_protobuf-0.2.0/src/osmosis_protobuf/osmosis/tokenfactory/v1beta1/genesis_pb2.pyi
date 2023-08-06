from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.tokenfactory.v1beta1 import authorityMetadata_pb2 as _authorityMetadata_pb2
from osmosis.tokenfactory.v1beta1 import params_pb2 as _params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisDenom(_message.Message):
    __slots__ = ['authority_metadata', 'denom']
    AUTHORITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    authority_metadata: _authorityMetadata_pb2.DenomAuthorityMetadata
    denom: str

    def __init__(self, denom: _Optional[str]=..., authority_metadata: _Optional[_Union[_authorityMetadata_pb2.DenomAuthorityMetadata, _Mapping]]=...) -> None:
        ...

class GenesisState(_message.Message):
    __slots__ = ['factory_denoms', 'params']
    FACTORY_DENOMS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    factory_denoms: _containers.RepeatedCompositeFieldContainer[GenesisDenom]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]]=..., factory_denoms: _Optional[_Iterable[_Union[GenesisDenom, _Mapping]]]=...) -> None:
        ...