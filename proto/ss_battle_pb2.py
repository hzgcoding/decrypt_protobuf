# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ss_battle.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ss_protoid_pb2
import cm_battletype_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ss_battle.proto',
  package='SProtoSpace',
  serialized_pb='\n\x0fss_battle.proto\x12\x0bSProtoSpace\x1a\x10ss_protoid.proto\x1a\x13\x63m_battletype.proto\"\xb5\x01\n\x14gs_create_battle_req\x12\x41\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x17gs_create_battle_req_id\x12\x13\n\x0b\x62\x61ttle_uuid\x18\x02 \x01(\x04\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.SProtoSpace.create_battle_data\x12\x16\n\x0esource_game_id\x18\x04 \x01(\x04\"\x93\x01\n\x14gs_create_battle_ack\x12\x41\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x17gs_create_battle_ack_id\x12\x13\n\x0b\x62\x61ttle_uuid\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\x05\x12\x16\n\x0esource_game_id\x18\x04 \x01(\x04\"\x9a\x01\n\x14\x63heck_pve_result_req\x12\x41\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x17\x63heck_pve_result_req_id\x12\x0f\n\x07role_id\x18\x02 \x01(\x04\x12.\n\x03req\x18\x03 \x01(\x0b\x32!.SProtoSpace.gs_create_battle_req\"\xa7\x01\n\x14\x63heck_pve_result_ack\x12\x41\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x17\x63heck_pve_result_ack_id\x12\x0f\n\x07role_id\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\r\x12.\n\x03req\x18\x04 \x01(\x0b\x32!.SProtoSpace.gs_create_battle_req\"\xc3\x01\n\x1bgs_create_office_battle_req\x12H\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x1egs_create_office_battle_req_id\x12\x13\n\x0b\x62\x61ttle_uuid\x18\x02 \x01(\x04\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.SProtoSpace.create_battle_data\x12\x16\n\x0esource_game_id\x18\x04 \x01(\x04\"\xa1\x01\n\x1bgs_create_office_battle_ack\x12H\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x1egs_create_office_battle_ack_id\x12\x13\n\x0b\x62\x61ttle_uuid\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\x05\x12\x16\n\x0esource_game_id\x18\x04 \x01(\x04\"\xf5\x01\n\x18gs_office_battle_end_ntf\x12\x45\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x1bgs_office_battle_end_ntf_id\x12\x13\n\x0b\x62\x61ttle_uuid\x18\x02 \x01(\x04\x12\x13\n\x0b\x62\x61ttle_type\x18\x03 \x01(\r\x12\x11\n\twinner_id\x18\x04 \x01(\x04\x12\x16\n\x0ewinner_camp_id\x18\x05 \x01(\x05\x12%\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32\x17.SProtoSpace.round_data\x12\x16\n\x0etarget_game_id\x18\x07 \x01(\x04')




_GS_CREATE_BATTLE_REQ = _descriptor.Descriptor(
  name='gs_create_battle_req',
  full_name='SProtoSpace.gs_create_battle_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gs_create_battle_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_uuid', full_name='SProtoSpace.gs_create_battle_req.battle_uuid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='SProtoSpace.gs_create_battle_req.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_game_id', full_name='SProtoSpace.gs_create_battle_req.source_game_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=72,
  serialized_end=253,
)


_GS_CREATE_BATTLE_ACK = _descriptor.Descriptor(
  name='gs_create_battle_ack',
  full_name='SProtoSpace.gs_create_battle_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gs_create_battle_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=401,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_uuid', full_name='SProtoSpace.gs_create_battle_ack.battle_uuid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SProtoSpace.gs_create_battle_ack.ret', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_game_id', full_name='SProtoSpace.gs_create_battle_ack.source_game_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=256,
  serialized_end=403,
)


_CHECK_PVE_RESULT_REQ = _descriptor.Descriptor(
  name='check_pve_result_req',
  full_name='SProtoSpace.check_pve_result_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.check_pve_result_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=402,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='SProtoSpace.check_pve_result_req.role_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req', full_name='SProtoSpace.check_pve_result_req.req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=406,
  serialized_end=560,
)


_CHECK_PVE_RESULT_ACK = _descriptor.Descriptor(
  name='check_pve_result_ack',
  full_name='SProtoSpace.check_pve_result_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.check_pve_result_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=403,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='SProtoSpace.check_pve_result_ack.role_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SProtoSpace.check_pve_result_ack.ret', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req', full_name='SProtoSpace.check_pve_result_ack.req', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=563,
  serialized_end=730,
)


_GS_CREATE_OFFICE_BATTLE_REQ = _descriptor.Descriptor(
  name='gs_create_office_battle_req',
  full_name='SProtoSpace.gs_create_office_battle_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gs_create_office_battle_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=404,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_uuid', full_name='SProtoSpace.gs_create_office_battle_req.battle_uuid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='SProtoSpace.gs_create_office_battle_req.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_game_id', full_name='SProtoSpace.gs_create_office_battle_req.source_game_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=733,
  serialized_end=928,
)


_GS_CREATE_OFFICE_BATTLE_ACK = _descriptor.Descriptor(
  name='gs_create_office_battle_ack',
  full_name='SProtoSpace.gs_create_office_battle_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gs_create_office_battle_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=405,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_uuid', full_name='SProtoSpace.gs_create_office_battle_ack.battle_uuid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SProtoSpace.gs_create_office_battle_ack.ret', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_game_id', full_name='SProtoSpace.gs_create_office_battle_ack.source_game_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=931,
  serialized_end=1092,
)


_GS_OFFICE_BATTLE_END_NTF = _descriptor.Descriptor(
  name='gs_office_battle_end_ntf',
  full_name='SProtoSpace.gs_office_battle_end_ntf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gs_office_battle_end_ntf.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=406,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_uuid', full_name='SProtoSpace.gs_office_battle_end_ntf.battle_uuid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_type', full_name='SProtoSpace.gs_office_battle_end_ntf.battle_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='winner_id', full_name='SProtoSpace.gs_office_battle_end_ntf.winner_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='winner_camp_id', full_name='SProtoSpace.gs_office_battle_end_ntf.winner_camp_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='SProtoSpace.gs_office_battle_end_ntf.data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_game_id', full_name='SProtoSpace.gs_office_battle_end_ntf.target_game_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1095,
  serialized_end=1340,
)

_GS_CREATE_BATTLE_REQ.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_GS_CREATE_BATTLE_REQ.fields_by_name['data'].message_type = cm_battletype_pb2._CREATE_BATTLE_DATA
_GS_CREATE_BATTLE_ACK.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_CHECK_PVE_RESULT_REQ.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_CHECK_PVE_RESULT_REQ.fields_by_name['req'].message_type = _GS_CREATE_BATTLE_REQ
_CHECK_PVE_RESULT_ACK.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_CHECK_PVE_RESULT_ACK.fields_by_name['req'].message_type = _GS_CREATE_BATTLE_REQ
_GS_CREATE_OFFICE_BATTLE_REQ.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_GS_CREATE_OFFICE_BATTLE_REQ.fields_by_name['data'].message_type = cm_battletype_pb2._CREATE_BATTLE_DATA
_GS_CREATE_OFFICE_BATTLE_ACK.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_GS_OFFICE_BATTLE_END_NTF.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_GS_OFFICE_BATTLE_END_NTF.fields_by_name['data'].message_type = cm_battletype_pb2._ROUND_DATA
DESCRIPTOR.message_types_by_name['gs_create_battle_req'] = _GS_CREATE_BATTLE_REQ
DESCRIPTOR.message_types_by_name['gs_create_battle_ack'] = _GS_CREATE_BATTLE_ACK
DESCRIPTOR.message_types_by_name['check_pve_result_req'] = _CHECK_PVE_RESULT_REQ
DESCRIPTOR.message_types_by_name['check_pve_result_ack'] = _CHECK_PVE_RESULT_ACK
DESCRIPTOR.message_types_by_name['gs_create_office_battle_req'] = _GS_CREATE_OFFICE_BATTLE_REQ
DESCRIPTOR.message_types_by_name['gs_create_office_battle_ack'] = _GS_CREATE_OFFICE_BATTLE_ACK
DESCRIPTOR.message_types_by_name['gs_office_battle_end_ntf'] = _GS_OFFICE_BATTLE_END_NTF

class gs_create_battle_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GS_CREATE_BATTLE_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.gs_create_battle_req)

class gs_create_battle_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GS_CREATE_BATTLE_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.gs_create_battle_ack)

class check_pve_result_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECK_PVE_RESULT_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.check_pve_result_req)

class check_pve_result_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECK_PVE_RESULT_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.check_pve_result_ack)

class gs_create_office_battle_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GS_CREATE_OFFICE_BATTLE_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.gs_create_office_battle_req)

class gs_create_office_battle_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GS_CREATE_OFFICE_BATTLE_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.gs_create_office_battle_ack)

class gs_office_battle_end_ntf(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GS_OFFICE_BATTLE_END_NTF

  # @@protoc_insertion_point(class_scope:SProtoSpace.gs_office_battle_end_ntf)


# @@protoc_insertion_point(module_scope)
