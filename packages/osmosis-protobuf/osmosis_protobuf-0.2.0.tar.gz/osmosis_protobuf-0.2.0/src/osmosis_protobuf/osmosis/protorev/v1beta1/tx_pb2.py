"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....osmosis.protorev.v1beta1 import protorev_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_protorev__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/protorev/v1beta1/tx.proto\x12\x18osmosis.protorev.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\'osmosis/protorev/v1beta1/protorev.proto\x1a\x19cosmos_proto/cosmos.proto"\xa7\x01\n\x0fMsgSetHotRoutes\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x12[\n\nhot_routes\x18\x02 \x03(\x0b2,.osmosis.protorev.v1beta1.TokenPairArbRoutesB\x19\xf2\xde\x1f\x11yaml:"hot_routes"\xc8\xde\x1f\x00"\x19\n\x17MsgSetHotRoutesResponse"\x8a\x01\n\x16MsgSetDeveloperAccount\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x127\n\x11developer_account\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"developer_account"" \n\x1eMsgSetDeveloperAccountResponse"\xa6\x01\n\x11MsgSetPoolWeights\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x12X\n\x0cpool_weights\x18\x02 \x01(\x0b2%.osmosis.protorev.v1beta1.PoolWeightsB\x1b\xf2\xde\x1f\x13yaml:"pool_weights"\xc8\xde\x1f\x00"\x1b\n\x19MsgSetPoolWeightsResponse"\x96\x01\n\x18MsgSetMaxPoolPointsPerTx\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x12A\n\x16max_pool_points_per_tx\x18\x02 \x01(\x04B!\xf2\xde\x1f\x1dyaml:"max_pool_points_per_tx"""\n MsgSetMaxPoolPointsPerTxResponse"\x9f\x01\n\x1bMsgSetMaxPoolPointsPerBlock\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x12G\n\x19max_pool_points_per_block\x18\x02 \x01(\x04B$\xf2\xde\x1f yaml:"max_pool_points_per_block""%\n#MsgSetMaxPoolPointsPerBlockResponse"\xa1\x01\n\x10MsgSetBaseDenoms\x127\n\x05admin\x18\x01 \x01(\tB(\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString\x12T\n\x0bbase_denoms\x18\x02 \x03(\x0b2#.osmosis.protorev.v1beta1.BaseDenomB\x1a\xf2\xde\x1f\x12yaml:"base_denoms"\xc8\xde\x1f\x00"\x1a\n\x18MsgSetBaseDenomsResponse2\xb5\x08\n\x03Msg\x12\x9a\x01\n\x0cSetHotRoutes\x12).osmosis.protorev.v1beta1.MsgSetHotRoutes\x1a1.osmosis.protorev.v1beta1.MsgSetHotRoutesResponse",\x82\xd3\xe4\x93\x02&"$/osmosis/v14/protorev/set_hot_routes\x12\xb6\x01\n\x13SetDeveloperAccount\x120.osmosis.protorev.v1beta1.MsgSetDeveloperAccount\x1a8.osmosis.protorev.v1beta1.MsgSetDeveloperAccountResponse"3\x82\xd3\xe4\x93\x02-"+/osmosis/v14/protorev/set_developer_account\x12\xc1\x01\n\x15SetMaxPoolPointsPerTx\x122.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTx\x1a:.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTxResponse"8\x82\xd3\xe4\x93\x022"0/osmosis/v14/protorev/set_max_pool_points_per_tx\x12\xcd\x01\n\x18SetMaxPoolPointsPerBlock\x125.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlock\x1a=.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlockResponse";\x82\xd3\xe4\x93\x025"3/osmosis/v14/protorev/set_max_pool_points_per_block\x12\xa2\x01\n\x0eSetPoolWeights\x12+.osmosis.protorev.v1beta1.MsgSetPoolWeights\x1a3.osmosis.protorev.v1beta1.MsgSetPoolWeightsResponse".\x82\xd3\xe4\x93\x02("&/osmosis/v14/protorev/set_pool_weights\x12\x9e\x01\n\rSetBaseDenoms\x12*.osmosis.protorev.v1beta1.MsgSetBaseDenoms\x1a2.osmosis.protorev.v1beta1.MsgSetBaseDenomsResponse"-\x82\xd3\xe4\x93\x02\'"%/osmosis/v14/protorev/set_base_denomsB6Z4github.com/osmosis-labs/osmosis/v15/x/protorev/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.protorev.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/osmosis-labs/osmosis/v15/x/protorev/types'
    _MSGSETHOTROUTES.fields_by_name['admin']._options = None
    _MSGSETHOTROUTES.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETHOTROUTES.fields_by_name['hot_routes']._options = None
    _MSGSETHOTROUTES.fields_by_name['hot_routes']._serialized_options = b'\xf2\xde\x1f\x11yaml:"hot_routes"\xc8\xde\x1f\x00'
    _MSGSETDEVELOPERACCOUNT.fields_by_name['admin']._options = None
    _MSGSETDEVELOPERACCOUNT.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETDEVELOPERACCOUNT.fields_by_name['developer_account']._options = None
    _MSGSETDEVELOPERACCOUNT.fields_by_name['developer_account']._serialized_options = b'\xf2\xde\x1f\x18yaml:"developer_account"'
    _MSGSETPOOLWEIGHTS.fields_by_name['admin']._options = None
    _MSGSETPOOLWEIGHTS.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETPOOLWEIGHTS.fields_by_name['pool_weights']._options = None
    _MSGSETPOOLWEIGHTS.fields_by_name['pool_weights']._serialized_options = b'\xf2\xde\x1f\x13yaml:"pool_weights"\xc8\xde\x1f\x00'
    _MSGSETMAXPOOLPOINTSPERTX.fields_by_name['admin']._options = None
    _MSGSETMAXPOOLPOINTSPERTX.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETMAXPOOLPOINTSPERTX.fields_by_name['max_pool_points_per_tx']._options = None
    _MSGSETMAXPOOLPOINTSPERTX.fields_by_name['max_pool_points_per_tx']._serialized_options = b'\xf2\xde\x1f\x1dyaml:"max_pool_points_per_tx"'
    _MSGSETMAXPOOLPOINTSPERBLOCK.fields_by_name['admin']._options = None
    _MSGSETMAXPOOLPOINTSPERBLOCK.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETMAXPOOLPOINTSPERBLOCK.fields_by_name['max_pool_points_per_block']._options = None
    _MSGSETMAXPOOLPOINTSPERBLOCK.fields_by_name['max_pool_points_per_block']._serialized_options = b'\xf2\xde\x1f yaml:"max_pool_points_per_block"'
    _MSGSETBASEDENOMS.fields_by_name['admin']._options = None
    _MSGSETBASEDENOMS.fields_by_name['admin']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"admin"\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETBASEDENOMS.fields_by_name['base_denoms']._options = None
    _MSGSETBASEDENOMS.fields_by_name['base_denoms']._serialized_options = b'\xf2\xde\x1f\x12yaml:"base_denoms"\xc8\xde\x1f\x00'
    _MSG.methods_by_name['SetHotRoutes']._options = None
    _MSG.methods_by_name['SetHotRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02&"$/osmosis/v14/protorev/set_hot_routes'
    _MSG.methods_by_name['SetDeveloperAccount']._options = None
    _MSG.methods_by_name['SetDeveloperAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/osmosis/v14/protorev/set_developer_account'
    _MSG.methods_by_name['SetMaxPoolPointsPerTx']._options = None
    _MSG.methods_by_name['SetMaxPoolPointsPerTx']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/osmosis/v14/protorev/set_max_pool_points_per_tx'
    _MSG.methods_by_name['SetMaxPoolPointsPerBlock']._options = None
    _MSG.methods_by_name['SetMaxPoolPointsPerBlock']._serialized_options = b'\x82\xd3\xe4\x93\x025"3/osmosis/v14/protorev/set_max_pool_points_per_block'
    _MSG.methods_by_name['SetPoolWeights']._options = None
    _MSG.methods_by_name['SetPoolWeights']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/osmosis/v14/protorev/set_pool_weights'
    _MSG.methods_by_name['SetBaseDenoms']._options = None
    _MSG.methods_by_name['SetBaseDenoms']._serialized_options = b'\x82\xd3\xe4\x93\x02\'"%/osmosis/v14/protorev/set_base_denoms'
    _MSGSETHOTROUTES._serialized_start = 184
    _MSGSETHOTROUTES._serialized_end = 351
    _MSGSETHOTROUTESRESPONSE._serialized_start = 353
    _MSGSETHOTROUTESRESPONSE._serialized_end = 378
    _MSGSETDEVELOPERACCOUNT._serialized_start = 381
    _MSGSETDEVELOPERACCOUNT._serialized_end = 519
    _MSGSETDEVELOPERACCOUNTRESPONSE._serialized_start = 521
    _MSGSETDEVELOPERACCOUNTRESPONSE._serialized_end = 553
    _MSGSETPOOLWEIGHTS._serialized_start = 556
    _MSGSETPOOLWEIGHTS._serialized_end = 722
    _MSGSETPOOLWEIGHTSRESPONSE._serialized_start = 724
    _MSGSETPOOLWEIGHTSRESPONSE._serialized_end = 751
    _MSGSETMAXPOOLPOINTSPERTX._serialized_start = 754
    _MSGSETMAXPOOLPOINTSPERTX._serialized_end = 904
    _MSGSETMAXPOOLPOINTSPERTXRESPONSE._serialized_start = 906
    _MSGSETMAXPOOLPOINTSPERTXRESPONSE._serialized_end = 940
    _MSGSETMAXPOOLPOINTSPERBLOCK._serialized_start = 943
    _MSGSETMAXPOOLPOINTSPERBLOCK._serialized_end = 1102
    _MSGSETMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_start = 1104
    _MSGSETMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_end = 1141
    _MSGSETBASEDENOMS._serialized_start = 1144
    _MSGSETBASEDENOMS._serialized_end = 1305
    _MSGSETBASEDENOMSRESPONSE._serialized_start = 1307
    _MSGSETBASEDENOMSRESPONSE._serialized_end = 1333
    _MSG._serialized_start = 1336
    _MSG._serialized_end = 2413