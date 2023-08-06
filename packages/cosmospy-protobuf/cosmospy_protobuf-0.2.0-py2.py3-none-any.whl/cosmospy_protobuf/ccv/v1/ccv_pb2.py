"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10ccv/v1/ccv.proto\x12\x1ainterchain_security.ccv.v1\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x14gogoproto/gogo.proto\x1a\x1btendermint/abci/types.proto"\xab\x01\n\x1cValidatorSetChangePacketData\x12]\n\x11validator_updates\x18\x01 \x03(\x0b2 .tendermint.abci.ValidatorUpdateB \xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"validator_updates"\x12\x18\n\x10valset_update_id\x18\x02 \x01(\x04\x12\x12\n\nslash_acks\x18\x03 \x03(\t"i\n\x19ValidatorSetChangePackets\x12L\n\x04list\x18\x01 \x03(\x0b28.interchain_security.ccv.v1.ValidatorSetChangePacketDataB\x04\xc8\xde\x1f\x00"0\n\x14VSCMaturedPacketData\x12\x18\n\x10valset_update_id\x18\x01 \x01(\x04"\xb0\x01\n\x0fSlashPacketData\x12G\n\tvalidator\x18\x01 \x01(\x0b2\x1a.tendermint.abci.ValidatorB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"validator"\x12\x18\n\x10valset_update_id\x18\x02 \x01(\x04\x12:\n\ninfraction\x18\x03 \x01(\x0e2&.cosmos.staking.v1beta1.InfractionType""\n\x13MaturedUnbondingOps\x12\x0b\n\x03ids\x18\x01 \x03(\x04"\xf8\x01\n\x12ConsumerPacketData\x12@\n\x04type\x18\x01 \x01(\x0e22.interchain_security.ccv.v1.ConsumerPacketDataType\x12F\n\x0fslashPacketData\x18\x02 \x01(\x0b2+.interchain_security.ccv.v1.SlashPacketDataH\x00\x12P\n\x14vscMaturedPacketData\x18\x03 \x01(\x0b20.interchain_security.ccv.v1.VSCMaturedPacketDataH\x00B\x06\n\x04data"\\\n\x16ConsumerPacketDataList\x12B\n\x04list\x18\x01 \x03(\x0b2..interchain_security.ccv.v1.ConsumerPacketDataB\x04\xc8\xde\x1f\x00*\xc1\x01\n\x16ConsumerPacketDataType\x12;\n CONSUMER_PACKET_TYPE_UNSPECIFIED\x10\x00\x1a\x15\x8a\x9d \x11UnspecifiedPacket\x12/\n\x1aCONSUMER_PACKET_TYPE_SLASH\x10\x01\x1a\x0f\x8a\x9d \x0bSlashPacket\x123\n\x19CONSUMER_PACKET_TYPE_VSCM\x10\x02\x1a\x14\x8a\x9d \x10VscMaturedPacket\x1a\x04\x88\xa3\x1e\x00B3Z1github.com/cosmos/interchain-security/x/ccv/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ccv.v1.ccv_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/interchain-security/x/ccv/types'
    _CONSUMERPACKETDATATYPE._options = None
    _CONSUMERPACKETDATATYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_UNSPECIFIED']._options = None
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x11UnspecifiedPacket'
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_SLASH']._options = None
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_SLASH']._serialized_options = b'\x8a\x9d \x0bSlashPacket'
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_VSCM']._options = None
    _CONSUMERPACKETDATATYPE.values_by_name['CONSUMER_PACKET_TYPE_VSCM']._serialized_options = b'\x8a\x9d \x10VscMaturedPacket'
    _VALIDATORSETCHANGEPACKETDATA.fields_by_name['validator_updates']._options = None
    _VALIDATORSETCHANGEPACKETDATA.fields_by_name['validator_updates']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"validator_updates"'
    _VALIDATORSETCHANGEPACKETS.fields_by_name['list']._options = None
    _VALIDATORSETCHANGEPACKETS.fields_by_name['list']._serialized_options = b'\xc8\xde\x1f\x00'
    _SLASHPACKETDATA.fields_by_name['validator']._options = None
    _SLASHPACKETDATA.fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"validator"'
    _CONSUMERPACKETDATALIST.fields_by_name['list']._options = None
    _CONSUMERPACKETDATALIST.fields_by_name['list']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSUMERPACKETDATATYPE._serialized_start = 1029
    _CONSUMERPACKETDATATYPE._serialized_end = 1222
    _VALIDATORSETCHANGEPACKETDATA._serialized_start = 138
    _VALIDATORSETCHANGEPACKETDATA._serialized_end = 309
    _VALIDATORSETCHANGEPACKETS._serialized_start = 311
    _VALIDATORSETCHANGEPACKETS._serialized_end = 416
    _VSCMATUREDPACKETDATA._serialized_start = 418
    _VSCMATUREDPACKETDATA._serialized_end = 466
    _SLASHPACKETDATA._serialized_start = 469
    _SLASHPACKETDATA._serialized_end = 645
    _MATUREDUNBONDINGOPS._serialized_start = 647
    _MATUREDUNBONDINGOPS._serialized_end = 681
    _CONSUMERPACKETDATA._serialized_start = 684
    _CONSUMERPACKETDATA._serialized_end = 932
    _CONSUMERPACKETDATALIST._serialized_start = 934
    _CONSUMERPACKETDATALIST._serialized_end = 1026