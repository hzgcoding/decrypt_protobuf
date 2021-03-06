# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs_mail.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import cm_roletype_pb2
import cm_battletype_pb2
import cm_activitytype_pb2
import cm_socialtype_pb2
import cs_protoid_pb2
import cs_errorcode_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs_mail.proto',
  package='SProtoSpace',
  serialized_pb='\n\rcs_mail.proto\x12\x0bSProtoSpace\x1a\x11\x63m_roletype.proto\x1a\x13\x63m_battletype.proto\x1a\x15\x63m_activitytype.proto\x1a\x13\x63m_socialtype.proto\x1a\x10\x63s_protoid.proto\x1a\x12\x63s_errorcode.proto\"o\n\x15mail_del_all_type_req\x12\x42\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x18mail_del_all_type_req_id\x12\x12\n\nmail_uuids\x18\x02 \x03(\x04\"\x88\x01\n\x15mail_del_all_type_ack\x12\x42\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x18mail_del_all_type_ack_id\x12\x12\n\nmail_uuids\x18\x02 \x03(\x04\x12\x17\n\x0f\x66\x61il_mail_uuids\x18\x03 \x03(\x04\"\xb4\x01\n\x1email_set_multi_mail_status_req\x12K\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:!mail_set_multi_mail_status_req_id\x12\x12\n\nmail_uuids\x18\x02 \x03(\x04\x12\x13\n\x0bto_set_read\x18\x03 \x01(\x08\x12\x1c\n\x14to_set_attach_getted\x18\x04 \x01(\x08\"\xfb\x01\n\x1email_set_multi_mail_status_ack\x12K\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:!mail_set_multi_mail_status_ack_id\x12\x12\n\nmail_uuids\x18\x02 \x03(\x04\x12\x13\n\x0bto_set_read\x18\x03 \x01(\x08\x12\x1c\n\x14to_set_attach_getted\x18\x04 \x01(\x08\x12\x17\n\x0f\x66\x61il_mail_uuids\x18\x05 \x03(\x04\x12,\n\trec_codes\x18\x06 \x01(\x0e\x32\x19.SProtoSpace.MsgErrorType\"\xd9\x01\n\x1amail_send_private_mail_req\x12G\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x1dmail_send_private_mail_req_id\x12(\n\x04mail\x18\x02 \x01(\x0b\x32\x1a.SProtoSpace.mail_instance\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x12\n\nto_role_id\x18\x05 \x01(\x04\x12\x14\n\x0cto_role_name\x18\x06 \x01(\t\"\x92\x01\n\x1amail_send_private_mail_ack\x12G\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x1dmail_send_private_mail_ack_id\x12+\n\x08rec_code\x18\x02 \x01(\x0e\x32\x19.SProtoSpace.MsgErrorType\"~\n\x11mail_all_type_ntf\x12>\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x14mail_all_type_ntf_id\x12)\n\x05mails\x18\x02 \x03(\x0b\x32\x1a.SProtoSpace.mail_instance\"o\n\x15mail_del_all_type_ntf\x12\x42\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\x18mail_del_all_type_ntf_id\x12\x12\n\nmail_uuids\x18\x02 \x03(\x04\"\x8e\x01\n\x1fmail_send_global_mail_debug_req\x12L\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\"mail_send_global_mail_debug_req_id\x12\x1d\n\x15global_mail_config_id\x18\x02 \x01(\x05\"\xcf\x02\n mail_send_private_mail_debug_req\x12M\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:#mail_send_private_mail_debug_req_id\x12\x1c\n\x14is_send_private_mail\x18\x03 \x01(\x05\x12\x1b\n\x13is_send_system_mail\x18\x04 \x01(\x05\x12\x14\n\x0cto_role_name\x18\x05 \x01(\t\x12\x12\n\nto_role_id\x18\x06 \x01(\x04\x12\x10\n\x08item_ids\x18\x07 \x03(\x05\x12\x13\n\x0bitem_counts\x18\x08 \x03(\x05\x12\r\n\x05title\x18\t \x01(\t\x12\x0f\n\x07\x63ontent\x18\n \x01(\t\x12\x11\n\tconfig_id\x18\x0b \x01(\x05\x12\x1d\n\x15is_public_server_test\x18\x0c \x01(\x05\"\x83\x01\n mail_send_private_mail_debug_ack\x12M\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:#mail_send_private_mail_debug_ack_id\x12\x10\n\x08rec_code\x18\x02 \x01(\x11\"\x81\x01\n\x1fmail_send_global_mail_debug_ack\x12L\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\"mail_send_global_mail_debug_ack_id\x12\x10\n\x08rec_code\x18\x02 \x01(\x11\"\xab\x01\n\x1email_send_group_mail_debug_req\x12K\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:!mail_send_group_mail_debug_req_id\x12\x1e\n\x16group_mail_to_role_ids\x18\x02 \x03(\x04\x12\x1c\n\x14group_mail_config_id\x18\x03 \x01(\x05\"\x7f\n\x1email_send_group_mail_debug_ack\x12K\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:!mail_send_group_mail_debug_ack_id\x12\x10\n\x08rec_code\x18\x02 \x01(\x11\"\xad\x01\n\x1fmail_send_family_mail_debug_req\x12L\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\"mail_send_family_mail_debug_req_id\x12\x1d\n\x15\x66\x61mily_mail_family_id\x18\x02 \x01(\x04\x12\x1d\n\x15\x66\x61mily_mail_config_id\x18\x03 \x01(\x05\"\x81\x01\n\x1fmail_send_family_mail_debug_ack\x12L\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ECSProtoID:\"mail_send_family_mail_debug_ack_id\x12\x10\n\x08rec_code\x18\x02 \x01(\x11')




_MAIL_DEL_ALL_TYPE_REQ = _descriptor.Descriptor(
  name='mail_del_all_type_req',
  full_name='SProtoSpace.mail_del_all_type_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_del_all_type_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5973,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_uuids', full_name='SProtoSpace.mail_del_all_type_req.mail_uuids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=152,
  serialized_end=263,
)


_MAIL_DEL_ALL_TYPE_ACK = _descriptor.Descriptor(
  name='mail_del_all_type_ack',
  full_name='SProtoSpace.mail_del_all_type_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_del_all_type_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5974,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_uuids', full_name='SProtoSpace.mail_del_all_type_ack.mail_uuids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fail_mail_uuids', full_name='SProtoSpace.mail_del_all_type_ack.fail_mail_uuids', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=266,
  serialized_end=402,
)


_MAIL_SET_MULTI_MAIL_STATUS_REQ = _descriptor.Descriptor(
  name='mail_set_multi_mail_status_req',
  full_name='SProtoSpace.mail_set_multi_mail_status_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_set_multi_mail_status_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5962,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_uuids', full_name='SProtoSpace.mail_set_multi_mail_status_req.mail_uuids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_set_read', full_name='SProtoSpace.mail_set_multi_mail_status_req.to_set_read', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_set_attach_getted', full_name='SProtoSpace.mail_set_multi_mail_status_req.to_set_attach_getted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=405,
  serialized_end=585,
)


_MAIL_SET_MULTI_MAIL_STATUS_ACK = _descriptor.Descriptor(
  name='mail_set_multi_mail_status_ack',
  full_name='SProtoSpace.mail_set_multi_mail_status_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_set_multi_mail_status_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5963,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_uuids', full_name='SProtoSpace.mail_set_multi_mail_status_ack.mail_uuids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_set_read', full_name='SProtoSpace.mail_set_multi_mail_status_ack.to_set_read', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_set_attach_getted', full_name='SProtoSpace.mail_set_multi_mail_status_ack.to_set_attach_getted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fail_mail_uuids', full_name='SProtoSpace.mail_set_multi_mail_status_ack.fail_mail_uuids', index=4,
      number=5, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_codes', full_name='SProtoSpace.mail_set_multi_mail_status_ack.rec_codes', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=588,
  serialized_end=839,
)


_MAIL_SEND_PRIVATE_MAIL_REQ = _descriptor.Descriptor(
  name='mail_send_private_mail_req',
  full_name='SProtoSpace.mail_send_private_mail_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_private_mail_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5964,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail', full_name='SProtoSpace.mail_send_private_mail_req.mail', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='SProtoSpace.mail_send_private_mail_req.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='SProtoSpace.mail_send_private_mail_req.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_role_id', full_name='SProtoSpace.mail_send_private_mail_req.to_role_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_role_name', full_name='SProtoSpace.mail_send_private_mail_req.to_role_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=842,
  serialized_end=1059,
)


_MAIL_SEND_PRIVATE_MAIL_ACK = _descriptor.Descriptor(
  name='mail_send_private_mail_ack',
  full_name='SProtoSpace.mail_send_private_mail_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_private_mail_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5965,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_code', full_name='SProtoSpace.mail_send_private_mail_ack.rec_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1062,
  serialized_end=1208,
)


_MAIL_ALL_TYPE_NTF = _descriptor.Descriptor(
  name='mail_all_type_ntf',
  full_name='SProtoSpace.mail_all_type_ntf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_all_type_ntf.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5972,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mails', full_name='SProtoSpace.mail_all_type_ntf.mails', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1210,
  serialized_end=1336,
)


_MAIL_DEL_ALL_TYPE_NTF = _descriptor.Descriptor(
  name='mail_del_all_type_ntf',
  full_name='SProtoSpace.mail_del_all_type_ntf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_del_all_type_ntf.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5975,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_uuids', full_name='SProtoSpace.mail_del_all_type_ntf.mail_uuids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1338,
  serialized_end=1449,
)


_MAIL_SEND_GLOBAL_MAIL_DEBUG_REQ = _descriptor.Descriptor(
  name='mail_send_global_mail_debug_req',
  full_name='SProtoSpace.mail_send_global_mail_debug_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_global_mail_debug_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5966,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_mail_config_id', full_name='SProtoSpace.mail_send_global_mail_debug_req.global_mail_config_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1452,
  serialized_end=1594,
)


_MAIL_SEND_PRIVATE_MAIL_DEBUG_REQ = _descriptor.Descriptor(
  name='mail_send_private_mail_debug_req',
  full_name='SProtoSpace.mail_send_private_mail_debug_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_private_mail_debug_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5976,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_send_private_mail', full_name='SProtoSpace.mail_send_private_mail_debug_req.is_send_private_mail', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_send_system_mail', full_name='SProtoSpace.mail_send_private_mail_debug_req.is_send_system_mail', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_role_name', full_name='SProtoSpace.mail_send_private_mail_debug_req.to_role_name', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_role_id', full_name='SProtoSpace.mail_send_private_mail_debug_req.to_role_id', index=4,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='SProtoSpace.mail_send_private_mail_debug_req.item_ids', index=5,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_counts', full_name='SProtoSpace.mail_send_private_mail_debug_req.item_counts', index=6,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='SProtoSpace.mail_send_private_mail_debug_req.title', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='SProtoSpace.mail_send_private_mail_debug_req.content', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_id', full_name='SProtoSpace.mail_send_private_mail_debug_req.config_id', index=9,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_public_server_test', full_name='SProtoSpace.mail_send_private_mail_debug_req.is_public_server_test', index=10,
      number=12, type=5, cpp_type=1, label=1,
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
  serialized_start=1597,
  serialized_end=1932,
)


_MAIL_SEND_PRIVATE_MAIL_DEBUG_ACK = _descriptor.Descriptor(
  name='mail_send_private_mail_debug_ack',
  full_name='SProtoSpace.mail_send_private_mail_debug_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_private_mail_debug_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5977,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_code', full_name='SProtoSpace.mail_send_private_mail_debug_ack.rec_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  serialized_start=1935,
  serialized_end=2066,
)


_MAIL_SEND_GLOBAL_MAIL_DEBUG_ACK = _descriptor.Descriptor(
  name='mail_send_global_mail_debug_ack',
  full_name='SProtoSpace.mail_send_global_mail_debug_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_global_mail_debug_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5967,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_code', full_name='SProtoSpace.mail_send_global_mail_debug_ack.rec_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  serialized_start=2069,
  serialized_end=2198,
)


_MAIL_SEND_GROUP_MAIL_DEBUG_REQ = _descriptor.Descriptor(
  name='mail_send_group_mail_debug_req',
  full_name='SProtoSpace.mail_send_group_mail_debug_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_group_mail_debug_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5968,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_mail_to_role_ids', full_name='SProtoSpace.mail_send_group_mail_debug_req.group_mail_to_role_ids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_mail_config_id', full_name='SProtoSpace.mail_send_group_mail_debug_req.group_mail_config_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=2201,
  serialized_end=2372,
)


_MAIL_SEND_GROUP_MAIL_DEBUG_ACK = _descriptor.Descriptor(
  name='mail_send_group_mail_debug_ack',
  full_name='SProtoSpace.mail_send_group_mail_debug_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_group_mail_debug_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5969,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_code', full_name='SProtoSpace.mail_send_group_mail_debug_ack.rec_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  serialized_start=2374,
  serialized_end=2501,
)


_MAIL_SEND_FAMILY_MAIL_DEBUG_REQ = _descriptor.Descriptor(
  name='mail_send_family_mail_debug_req',
  full_name='SProtoSpace.mail_send_family_mail_debug_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_family_mail_debug_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5970,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_mail_family_id', full_name='SProtoSpace.mail_send_family_mail_debug_req.family_mail_family_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_mail_config_id', full_name='SProtoSpace.mail_send_family_mail_debug_req.family_mail_config_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=2504,
  serialized_end=2677,
)


_MAIL_SEND_FAMILY_MAIL_DEBUG_ACK = _descriptor.Descriptor(
  name='mail_send_family_mail_debug_ack',
  full_name='SProtoSpace.mail_send_family_mail_debug_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.mail_send_family_mail_debug_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5971,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rec_code', full_name='SProtoSpace.mail_send_family_mail_debug_ack.rec_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  serialized_start=2680,
  serialized_end=2809,
)

_MAIL_DEL_ALL_TYPE_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_DEL_ALL_TYPE_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SET_MULTI_MAIL_STATUS_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SET_MULTI_MAIL_STATUS_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SET_MULTI_MAIL_STATUS_ACK.fields_by_name['rec_codes'].enum_type = cs_errorcode_pb2._MSGERRORTYPE
_MAIL_SEND_PRIVATE_MAIL_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_PRIVATE_MAIL_REQ.fields_by_name['mail'].message_type = cm_roletype_pb2._MAIL_INSTANCE
_MAIL_SEND_PRIVATE_MAIL_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_PRIVATE_MAIL_ACK.fields_by_name['rec_code'].enum_type = cs_errorcode_pb2._MSGERRORTYPE
_MAIL_ALL_TYPE_NTF.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_ALL_TYPE_NTF.fields_by_name['mails'].message_type = cm_roletype_pb2._MAIL_INSTANCE
_MAIL_DEL_ALL_TYPE_NTF.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_GLOBAL_MAIL_DEBUG_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_PRIVATE_MAIL_DEBUG_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_PRIVATE_MAIL_DEBUG_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_GLOBAL_MAIL_DEBUG_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_GROUP_MAIL_DEBUG_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_GROUP_MAIL_DEBUG_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_FAMILY_MAIL_DEBUG_REQ.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
_MAIL_SEND_FAMILY_MAIL_DEBUG_ACK.fields_by_name['protoid'].enum_type = cs_protoid_pb2._ECSPROTOID
DESCRIPTOR.message_types_by_name['mail_del_all_type_req'] = _MAIL_DEL_ALL_TYPE_REQ
DESCRIPTOR.message_types_by_name['mail_del_all_type_ack'] = _MAIL_DEL_ALL_TYPE_ACK
DESCRIPTOR.message_types_by_name['mail_set_multi_mail_status_req'] = _MAIL_SET_MULTI_MAIL_STATUS_REQ
DESCRIPTOR.message_types_by_name['mail_set_multi_mail_status_ack'] = _MAIL_SET_MULTI_MAIL_STATUS_ACK
DESCRIPTOR.message_types_by_name['mail_send_private_mail_req'] = _MAIL_SEND_PRIVATE_MAIL_REQ
DESCRIPTOR.message_types_by_name['mail_send_private_mail_ack'] = _MAIL_SEND_PRIVATE_MAIL_ACK
DESCRIPTOR.message_types_by_name['mail_all_type_ntf'] = _MAIL_ALL_TYPE_NTF
DESCRIPTOR.message_types_by_name['mail_del_all_type_ntf'] = _MAIL_DEL_ALL_TYPE_NTF
DESCRIPTOR.message_types_by_name['mail_send_global_mail_debug_req'] = _MAIL_SEND_GLOBAL_MAIL_DEBUG_REQ
DESCRIPTOR.message_types_by_name['mail_send_private_mail_debug_req'] = _MAIL_SEND_PRIVATE_MAIL_DEBUG_REQ
DESCRIPTOR.message_types_by_name['mail_send_private_mail_debug_ack'] = _MAIL_SEND_PRIVATE_MAIL_DEBUG_ACK
DESCRIPTOR.message_types_by_name['mail_send_global_mail_debug_ack'] = _MAIL_SEND_GLOBAL_MAIL_DEBUG_ACK
DESCRIPTOR.message_types_by_name['mail_send_group_mail_debug_req'] = _MAIL_SEND_GROUP_MAIL_DEBUG_REQ
DESCRIPTOR.message_types_by_name['mail_send_group_mail_debug_ack'] = _MAIL_SEND_GROUP_MAIL_DEBUG_ACK
DESCRIPTOR.message_types_by_name['mail_send_family_mail_debug_req'] = _MAIL_SEND_FAMILY_MAIL_DEBUG_REQ
DESCRIPTOR.message_types_by_name['mail_send_family_mail_debug_ack'] = _MAIL_SEND_FAMILY_MAIL_DEBUG_ACK

class mail_del_all_type_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_DEL_ALL_TYPE_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_del_all_type_req)

class mail_del_all_type_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_DEL_ALL_TYPE_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_del_all_type_ack)

class mail_set_multi_mail_status_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SET_MULTI_MAIL_STATUS_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_set_multi_mail_status_req)

class mail_set_multi_mail_status_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SET_MULTI_MAIL_STATUS_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_set_multi_mail_status_ack)

class mail_send_private_mail_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_PRIVATE_MAIL_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_private_mail_req)

class mail_send_private_mail_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_PRIVATE_MAIL_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_private_mail_ack)

class mail_all_type_ntf(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_ALL_TYPE_NTF

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_all_type_ntf)

class mail_del_all_type_ntf(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_DEL_ALL_TYPE_NTF

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_del_all_type_ntf)

class mail_send_global_mail_debug_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_GLOBAL_MAIL_DEBUG_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_global_mail_debug_req)

class mail_send_private_mail_debug_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_PRIVATE_MAIL_DEBUG_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_private_mail_debug_req)

class mail_send_private_mail_debug_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_PRIVATE_MAIL_DEBUG_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_private_mail_debug_ack)

class mail_send_global_mail_debug_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_GLOBAL_MAIL_DEBUG_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_global_mail_debug_ack)

class mail_send_group_mail_debug_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_GROUP_MAIL_DEBUG_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_group_mail_debug_req)

class mail_send_group_mail_debug_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_GROUP_MAIL_DEBUG_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_group_mail_debug_ack)

class mail_send_family_mail_debug_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_FAMILY_MAIL_DEBUG_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_family_mail_debug_req)

class mail_send_family_mail_debug_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_SEND_FAMILY_MAIL_DEBUG_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.mail_send_family_mail_debug_ack)


# @@protoc_insertion_point(module_scope)
