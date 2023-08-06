from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor
SuperfluidAssetTypeLPShare: SuperfluidAssetType
SuperfluidAssetTypeNative: SuperfluidAssetType

class LockIdIntermediaryAccountConnection(_message.Message):
    __slots__ = ['intermediary_account', 'lock_id']
    INTERMEDIARY_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    intermediary_account: str
    lock_id: int

    def __init__(self, lock_id: _Optional[int]=..., intermediary_account: _Optional[str]=...) -> None:
        ...

class OsmoEquivalentMultiplierRecord(_message.Message):
    __slots__ = ['denom', 'epoch_number', 'multiplier']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    denom: str
    epoch_number: int
    multiplier: str

    def __init__(self, epoch_number: _Optional[int]=..., denom: _Optional[str]=..., multiplier: _Optional[str]=...) -> None:
        ...

class SuperfluidAsset(_message.Message):
    __slots__ = ['asset_type', 'denom']
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    asset_type: SuperfluidAssetType
    denom: str

    def __init__(self, denom: _Optional[str]=..., asset_type: _Optional[_Union[SuperfluidAssetType, str]]=...) -> None:
        ...

class SuperfluidDelegationRecord(_message.Message):
    __slots__ = ['delegation_amount', 'delegator_address', 'equivalent_staked_amount', 'validator_address']
    DELEGATION_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EQUIVALENT_STAKED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegation_amount: _coin_pb2.Coin
    delegator_address: str
    equivalent_staked_amount: _coin_pb2.Coin
    validator_address: str

    def __init__(self, delegator_address: _Optional[str]=..., validator_address: _Optional[str]=..., delegation_amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., equivalent_staked_amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class SuperfluidIntermediaryAccount(_message.Message):
    __slots__ = ['denom', 'gauge_id', 'val_addr']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    GAUGE_ID_FIELD_NUMBER: _ClassVar[int]
    VAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    denom: str
    gauge_id: int
    val_addr: str

    def __init__(self, denom: _Optional[str]=..., val_addr: _Optional[str]=..., gauge_id: _Optional[int]=...) -> None:
        ...

class UnpoolWhitelistedPools(_message.Message):
    __slots__ = ['ids']
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class SuperfluidAssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []