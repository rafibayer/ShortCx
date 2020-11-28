# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apiservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apiservice.proto',
  package='protos',
  syntax='proto3',
  serialized_options=b'Z\007api;api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x61piservice.proto\x12\x06protos\"]\n\x11\x43reateUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x15\n\rpassword_conf\x18\x04 \x01(\t\"(\n\x12\x43reateUserResponse\x12\x12\n\nauth_token\x18\x01 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"#\n\rLoginResponse\x12\x12\n\nauth_token\x18\x01 \x01(\t\"#\n\rLogoutRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\"!\n\x0eLogoutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x15\x43reateShortcutRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\x12\x12\n\ntarget_url\x18\x02 \x01(\t\"+\n\x16\x43reateShortcutResponse\x12\x11\n\turl_token\x18\x01 \x01(\t\">\n\x15\x44\x65leteShortcutRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\x12\x11\n\turl_token\x18\x02 \x01(\t\")\n\x16\x44\x65leteShortcutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\'\n\x12GetShortcutRequest\x12\x11\n\turl_token\x18\x01 \x01(\t\")\n\x13GetShortcutResponse\x12\x12\n\ntarget_url\x18\x01 \x01(\t2\xb6\x03\n\nAPIService\x12\x45\n\nCreateUser\x12\x19.protos.CreateUserRequest\x1a\x1a.protos.CreateUserResponse\"\x00\x12\x36\n\x05Login\x12\x14.protos.LoginRequest\x1a\x15.protos.LoginResponse\"\x00\x12\x39\n\x06Logout\x12\x15.protos.LogoutRequest\x1a\x16.protos.LogoutResponse\"\x00\x12Q\n\x0e\x43reateShortcut\x12\x1d.protos.CreateShortcutRequest\x1a\x1e.protos.CreateShortcutResponse\"\x00\x12Q\n\x0e\x44\x65leteShortcut\x12\x1d.protos.DeleteShortcutRequest\x1a\x1e.protos.DeleteShortcutResponse\"\x00\x12H\n\x0bGetShortcut\x12\x1a.protos.GetShortcutRequest\x1a\x1b.protos.GetShortcutResponse\"\x00\x42\tZ\x07\x61pi;apib\x06proto3'
)




_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='protos.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='protos.CreateUserRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='protos.CreateUserRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='protos.CreateUserRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password_conf', full_name='protos.CreateUserRequest.password_conf', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=121,
)


_CREATEUSERRESPONSE = _descriptor.Descriptor(
  name='CreateUserResponse',
  full_name='protos.CreateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='protos.CreateUserResponse.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=123,
  serialized_end=163,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='protos.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='protos.LoginRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='protos.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=165,
  serialized_end=212,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='protos.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='protos.LoginResponse.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=214,
  serialized_end=249,
)


_LOGOUTREQUEST = _descriptor.Descriptor(
  name='LogoutRequest',
  full_name='protos.LogoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='protos.LogoutRequest.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=251,
  serialized_end=286,
)


_LOGOUTRESPONSE = _descriptor.Descriptor(
  name='LogoutResponse',
  full_name='protos.LogoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='protos.LogoutResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=288,
  serialized_end=321,
)


_CREATESHORTCUTREQUEST = _descriptor.Descriptor(
  name='CreateShortcutRequest',
  full_name='protos.CreateShortcutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='protos.CreateShortcutRequest.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_url', full_name='protos.CreateShortcutRequest.target_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=323,
  serialized_end=386,
)


_CREATESHORTCUTRESPONSE = _descriptor.Descriptor(
  name='CreateShortcutResponse',
  full_name='protos.CreateShortcutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url_token', full_name='protos.CreateShortcutResponse.url_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=388,
  serialized_end=431,
)


_DELETESHORTCUTREQUEST = _descriptor.Descriptor(
  name='DeleteShortcutRequest',
  full_name='protos.DeleteShortcutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='protos.DeleteShortcutRequest.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url_token', full_name='protos.DeleteShortcutRequest.url_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=433,
  serialized_end=495,
)


_DELETESHORTCUTRESPONSE = _descriptor.Descriptor(
  name='DeleteShortcutResponse',
  full_name='protos.DeleteShortcutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='protos.DeleteShortcutResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=497,
  serialized_end=538,
)


_GETSHORTCUTREQUEST = _descriptor.Descriptor(
  name='GetShortcutRequest',
  full_name='protos.GetShortcutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url_token', full_name='protos.GetShortcutRequest.url_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=540,
  serialized_end=579,
)


_GETSHORTCUTRESPONSE = _descriptor.Descriptor(
  name='GetShortcutResponse',
  full_name='protos.GetShortcutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_url', full_name='protos.GetShortcutResponse.target_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=581,
  serialized_end=622,
)

DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResponse'] = _CREATEUSERRESPONSE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['LogoutRequest'] = _LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['LogoutResponse'] = _LOGOUTRESPONSE
DESCRIPTOR.message_types_by_name['CreateShortcutRequest'] = _CREATESHORTCUTREQUEST
DESCRIPTOR.message_types_by_name['CreateShortcutResponse'] = _CREATESHORTCUTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteShortcutRequest'] = _DELETESHORTCUTREQUEST
DESCRIPTOR.message_types_by_name['DeleteShortcutResponse'] = _DELETESHORTCUTRESPONSE
DESCRIPTOR.message_types_by_name['GetShortcutRequest'] = _GETSHORTCUTREQUEST
DESCRIPTOR.message_types_by_name['GetShortcutResponse'] = _GETSHORTCUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

LogoutRequest = _reflection.GeneratedProtocolMessageType('LogoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogoutRequest)
  })
_sym_db.RegisterMessage(LogoutRequest)

LogoutResponse = _reflection.GeneratedProtocolMessageType('LogoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogoutResponse)
  })
_sym_db.RegisterMessage(LogoutResponse)

CreateShortcutRequest = _reflection.GeneratedProtocolMessageType('CreateShortcutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESHORTCUTREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateShortcutRequest)
  })
_sym_db.RegisterMessage(CreateShortcutRequest)

CreateShortcutResponse = _reflection.GeneratedProtocolMessageType('CreateShortcutResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESHORTCUTRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateShortcutResponse)
  })
_sym_db.RegisterMessage(CreateShortcutResponse)

DeleteShortcutRequest = _reflection.GeneratedProtocolMessageType('DeleteShortcutRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESHORTCUTREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeleteShortcutRequest)
  })
_sym_db.RegisterMessage(DeleteShortcutRequest)

DeleteShortcutResponse = _reflection.GeneratedProtocolMessageType('DeleteShortcutResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESHORTCUTRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeleteShortcutResponse)
  })
_sym_db.RegisterMessage(DeleteShortcutResponse)

GetShortcutRequest = _reflection.GeneratedProtocolMessageType('GetShortcutRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSHORTCUTREQUEST,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetShortcutRequest)
  })
_sym_db.RegisterMessage(GetShortcutRequest)

GetShortcutResponse = _reflection.GeneratedProtocolMessageType('GetShortcutResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSHORTCUTRESPONSE,
  '__module__' : 'apiservice_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetShortcutResponse)
  })
_sym_db.RegisterMessage(GetShortcutResponse)


DESCRIPTOR._options = None

_APISERVICE = _descriptor.ServiceDescriptor(
  name='APIService',
  full_name='protos.APIService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=625,
  serialized_end=1063,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='protos.APIService.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='protos.APIService.Login',
    index=1,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='protos.APIService.Logout',
    index=2,
    containing_service=None,
    input_type=_LOGOUTREQUEST,
    output_type=_LOGOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateShortcut',
    full_name='protos.APIService.CreateShortcut',
    index=3,
    containing_service=None,
    input_type=_CREATESHORTCUTREQUEST,
    output_type=_CREATESHORTCUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShortcut',
    full_name='protos.APIService.DeleteShortcut',
    index=4,
    containing_service=None,
    input_type=_DELETESHORTCUTREQUEST,
    output_type=_DELETESHORTCUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetShortcut',
    full_name='protos.APIService.GetShortcut',
    index=5,
    containing_service=None,
    input_type=_GETSHORTCUTREQUEST,
    output_type=_GETSHORTCUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APISERVICE)

DESCRIPTOR.services_by_name['APIService'] = _APISERVICE

# @@protoc_insertion_point(module_scope)