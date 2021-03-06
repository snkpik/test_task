# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: haberdasher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='haberdasher.proto',
  package='twitch.twirp.example',
  syntax='proto3',
  serialized_options=_b('Z\007example'),
  serialized_pb=_b('\n\x11haberdasher.proto\x12\x14twitch.twirp.example\"0\n\x03Hat\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x16\n\x04Size\x12\x0e\n\x06inches\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"\x1a\n\nDollarRate\x12\x0c\n\x04rate\x18\x01 \x01(\x02\x32\xa3\x01\n\x0bHaberdasher\x12\x44\n\x0bMakeHatTest\x12\x1a.twitch.twirp.example.Size\x1a\x19.twitch.twirp.example.Hat\x12N\n\rGetDollarRate\x12\x1b.twitch.twirp.example.Empty\x1a .twitch.twirp.example.DollarRateB\tZ\x07\x65xampleb\x06proto3')
)




_HAT = _descriptor.Descriptor(
  name='Hat',
  full_name='twitch.twirp.example.Hat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='twitch.twirp.example.Hat.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='twitch.twirp.example.Hat.color', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='twitch.twirp.example.Hat.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=91,
)


_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='twitch.twirp.example.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inches', full_name='twitch.twirp.example.Size.inches', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=115,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='twitch.twirp.example.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=124,
)


_DOLLARRATE = _descriptor.Descriptor(
  name='DollarRate',
  full_name='twitch.twirp.example.DollarRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate', full_name='twitch.twirp.example.DollarRate.rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['Hat'] = _HAT
DESCRIPTOR.message_types_by_name['Size'] = _SIZE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['DollarRate'] = _DOLLARRATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hat = _reflection.GeneratedProtocolMessageType('Hat', (_message.Message,), dict(
  DESCRIPTOR = _HAT,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.Hat)
  ))
_sym_db.RegisterMessage(Hat)

Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
  DESCRIPTOR = _SIZE,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.Size)
  ))
_sym_db.RegisterMessage(Size)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.Empty)
  ))
_sym_db.RegisterMessage(Empty)

DollarRate = _reflection.GeneratedProtocolMessageType('DollarRate', (_message.Message,), dict(
  DESCRIPTOR = _DOLLARRATE,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.DollarRate)
  ))
_sym_db.RegisterMessage(DollarRate)


DESCRIPTOR._options = None

_HABERDASHER = _descriptor.ServiceDescriptor(
  name='Haberdasher',
  full_name='twitch.twirp.example.Haberdasher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=155,
  serialized_end=318,
  methods=[
  _descriptor.MethodDescriptor(
    name='MakeHatTest',
    full_name='twitch.twirp.example.Haberdasher.MakeHatTest',
    index=0,
    containing_service=None,
    input_type=_SIZE,
    output_type=_HAT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDollarRate',
    full_name='twitch.twirp.example.Haberdasher.GetDollarRate',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_DOLLARRATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HABERDASHER)

DESCRIPTOR.services_by_name['Haberdasher'] = _HABERDASHER

# @@protoc_insertion_point(module_scope)
