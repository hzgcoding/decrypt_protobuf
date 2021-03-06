# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ss_login.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ss_protoid_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ss_login.proto',
  package='SProtoSpace',
  serialized_pb='\n\x0ess_login.proto\x12\x0bSProtoSpace\x1a\x10ss_protoid.proto\"U\n\x12gm2l_heartbeat_req\x12?\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x15gm2l_heartbeat_req_id\"U\n\x12l2gm_heartbeat_ack\x12?\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x15l2gm_heartbeat_ack_id\"M\n\x0egm2l_close_req\x12;\n\x07protoid\x18\x01 \x01(\x0e\x32\x17.SProtoSpace.ESSProtoID:\x11gm2l_close_req_id')




_GM2L_HEARTBEAT_REQ = _descriptor.Descriptor(
  name='gm2l_heartbeat_req',
  full_name='SProtoSpace.gm2l_heartbeat_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gm2l_heartbeat_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=70,
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
  serialized_start=49,
  serialized_end=134,
)


_L2GM_HEARTBEAT_ACK = _descriptor.Descriptor(
  name='l2gm_heartbeat_ack',
  full_name='SProtoSpace.l2gm_heartbeat_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.l2gm_heartbeat_ack.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=71,
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
  serialized_start=136,
  serialized_end=221,
)


_GM2L_CLOSE_REQ = _descriptor.Descriptor(
  name='gm2l_close_req',
  full_name='SProtoSpace.gm2l_close_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protoid', full_name='SProtoSpace.gm2l_close_req.protoid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=72,
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
  serialized_start=223,
  serialized_end=300,
)

_GM2L_HEARTBEAT_REQ.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_L2GM_HEARTBEAT_ACK.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
_GM2L_CLOSE_REQ.fields_by_name['protoid'].enum_type = ss_protoid_pb2._ESSPROTOID
DESCRIPTOR.message_types_by_name['gm2l_heartbeat_req'] = _GM2L_HEARTBEAT_REQ
DESCRIPTOR.message_types_by_name['l2gm_heartbeat_ack'] = _L2GM_HEARTBEAT_ACK
DESCRIPTOR.message_types_by_name['gm2l_close_req'] = _GM2L_CLOSE_REQ

class gm2l_heartbeat_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GM2L_HEARTBEAT_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.gm2l_heartbeat_req)

class l2gm_heartbeat_ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _L2GM_HEARTBEAT_ACK

  # @@protoc_insertion_point(class_scope:SProtoSpace.l2gm_heartbeat_ack)

class gm2l_close_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GM2L_CLOSE_REQ

  # @@protoc_insertion_point(class_scope:SProtoSpace.gm2l_close_req)


# @@protoc_insertion_point(module_scope)
