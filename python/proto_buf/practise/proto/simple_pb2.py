# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple.proto',
  package='example.simple',
  syntax='proto3',
  serialized_pb=_b('\n\x0csimple.proto\x12\x0e\x65xample.simple\"K\n\x06Simple\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\tis_simple\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0csample_lists\x18\x04 \x03(\rb\x06proto3')
)




_SIMPLE = _descriptor.Descriptor(
  name='Simple',
  full_name='example.simple.Simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='example.simple.Simple.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_simple', full_name='example.simple.Simple.is_simple', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='example.simple.Simple.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_lists', full_name='example.simple.Simple.sample_lists', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Simple'] = _SIMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Simple = _reflection.GeneratedProtocolMessageType('Simple', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLE,
  __module__ = 'simple_pb2'
  # @@protoc_insertion_point(class_scope:example.simple.Simple)
  ))
_sym_db.RegisterMessage(Simple)


# @@protoc_insertion_point(module_scope)
