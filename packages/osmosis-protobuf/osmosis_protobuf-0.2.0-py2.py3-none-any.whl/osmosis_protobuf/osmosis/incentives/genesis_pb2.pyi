from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from osmosis.incentives import params_pb2 as _params_pb2
from osmosis.incentives import gauge_pb2 as _gauge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['gauges', 'last_gauge_id', 'lockable_durations', 'params']
    GAUGES_FIELD_NUMBER: _ClassVar[int]
    LAST_GAUGE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCKABLE_DURATIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    gauges: _containers.RepeatedCompositeFieldContainer[_gauge_pb2.Gauge]
    last_gauge_id: int
    lockable_durations: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]]=..., gauges: _Optional[_Iterable[_Union[_gauge_pb2.Gauge, _Mapping]]]=..., lockable_durations: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., last_gauge_id: _Optional[int]=...) -> None:
        ...