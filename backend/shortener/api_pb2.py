# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x04main\".\n\x11shortenURLRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04slug\x18\x02 \x01(\t\"5\n\x12shortenURLResponse\x12\x10\n\x08shortURL\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"%\n\x15\x63heckIfPresentRequest\x12\x0c\n\x04slug\x18\x01 \x01(\t\":\n\x16\x63heckIfPresentResponse\x12\x11\n\tisPresent\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"-\n\x10storeInDBRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04slug\x18\x02 \x01(\t\"5\n\x11storeInDBResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\'\n\x17\x66\x65tchURLFromSlugRequest\x12\x0c\n\x04slug\x18\x01 \x01(\t\"6\n\x18\x66\x65tchURLFromSlugResponse\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2N\n\tShortener\x12\x41\n\nshortenURL\x12\x17.main.shortenURLRequest\x1a\x18.main.shortenURLResponse\"\x00\x32\xee\x01\n\x08\x44\x61tabase\x12M\n\x0e\x63heckIfPresent\x12\x1b.main.checkIfPresentRequest\x1a\x1c.main.checkIfPresentResponse\"\x00\x12>\n\tstoreInDB\x12\x16.main.storeInDBRequest\x1a\x17.main.storeInDBResponse\"\x00\x12S\n\x10\x66\x65tchURLFromSlug\x12\x1d.main.fetchURLFromSlugRequest\x1a\x1e.main.fetchURLFromSlugResponse\"\x00\x42\tZ\x07./apiPbb\x06proto3')



_SHORTENURLREQUEST = DESCRIPTOR.message_types_by_name['shortenURLRequest']
_SHORTENURLRESPONSE = DESCRIPTOR.message_types_by_name['shortenURLResponse']
_CHECKIFPRESENTREQUEST = DESCRIPTOR.message_types_by_name['checkIfPresentRequest']
_CHECKIFPRESENTRESPONSE = DESCRIPTOR.message_types_by_name['checkIfPresentResponse']
_STOREINDBREQUEST = DESCRIPTOR.message_types_by_name['storeInDBRequest']
_STOREINDBRESPONSE = DESCRIPTOR.message_types_by_name['storeInDBResponse']
_FETCHURLFROMSLUGREQUEST = DESCRIPTOR.message_types_by_name['fetchURLFromSlugRequest']
_FETCHURLFROMSLUGRESPONSE = DESCRIPTOR.message_types_by_name['fetchURLFromSlugResponse']
shortenURLRequest = _reflection.GeneratedProtocolMessageType('shortenURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHORTENURLREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.shortenURLRequest)
  })
_sym_db.RegisterMessage(shortenURLRequest)

shortenURLResponse = _reflection.GeneratedProtocolMessageType('shortenURLResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHORTENURLRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.shortenURLResponse)
  })
_sym_db.RegisterMessage(shortenURLResponse)

checkIfPresentRequest = _reflection.GeneratedProtocolMessageType('checkIfPresentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIFPRESENTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.checkIfPresentRequest)
  })
_sym_db.RegisterMessage(checkIfPresentRequest)

checkIfPresentResponse = _reflection.GeneratedProtocolMessageType('checkIfPresentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIFPRESENTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.checkIfPresentResponse)
  })
_sym_db.RegisterMessage(checkIfPresentResponse)

storeInDBRequest = _reflection.GeneratedProtocolMessageType('storeInDBRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOREINDBREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.storeInDBRequest)
  })
_sym_db.RegisterMessage(storeInDBRequest)

storeInDBResponse = _reflection.GeneratedProtocolMessageType('storeInDBResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOREINDBRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.storeInDBResponse)
  })
_sym_db.RegisterMessage(storeInDBResponse)

fetchURLFromSlugRequest = _reflection.GeneratedProtocolMessageType('fetchURLFromSlugRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHURLFROMSLUGREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.fetchURLFromSlugRequest)
  })
_sym_db.RegisterMessage(fetchURLFromSlugRequest)

fetchURLFromSlugResponse = _reflection.GeneratedProtocolMessageType('fetchURLFromSlugResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHURLFROMSLUGRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:main.fetchURLFromSlugResponse)
  })
_sym_db.RegisterMessage(fetchURLFromSlugResponse)

_SHORTENER = DESCRIPTOR.services_by_name['Shortener']
_DATABASE = DESCRIPTOR.services_by_name['Database']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007./apiPb'
  _SHORTENURLREQUEST._serialized_start=19
  _SHORTENURLREQUEST._serialized_end=65
  _SHORTENURLRESPONSE._serialized_start=67
  _SHORTENURLRESPONSE._serialized_end=120
  _CHECKIFPRESENTREQUEST._serialized_start=122
  _CHECKIFPRESENTREQUEST._serialized_end=159
  _CHECKIFPRESENTRESPONSE._serialized_start=161
  _CHECKIFPRESENTRESPONSE._serialized_end=219
  _STOREINDBREQUEST._serialized_start=221
  _STOREINDBREQUEST._serialized_end=266
  _STOREINDBRESPONSE._serialized_start=268
  _STOREINDBRESPONSE._serialized_end=321
  _FETCHURLFROMSLUGREQUEST._serialized_start=323
  _FETCHURLFROMSLUGREQUEST._serialized_end=362
  _FETCHURLFROMSLUGRESPONSE._serialized_start=364
  _FETCHURLFROMSLUGRESPONSE._serialized_end=418
  _SHORTENER._serialized_start=420
  _SHORTENER._serialized_end=498
  _DATABASE._serialized_start=501
  _DATABASE._serialized_end=739
# @@protoc_insertion_point(module_scope)
