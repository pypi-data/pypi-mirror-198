# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/graph_debug_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/tensorflow/core/protobuf/graph_debug_info.proto\x12\ntensorflow\"\xd5\x02\n\x0eGraphDebugInfo\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x36\n\x06traces\x18\x02 \x03(\x0b\x32&.tensorflow.GraphDebugInfo.TracesEntry\x1aX\n\x0b\x46ileLineCol\x12\x12\n\nfile_index\x18\x01 \x01(\x05\x12\x0c\n\x04line\x18\x02 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x03 \x01(\x05\x12\x0c\n\x04\x66unc\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\x1aL\n\nStackTrace\x12>\n\x0e\x66ile_line_cols\x18\x01 \x03(\x0b\x32&.tensorflow.GraphDebugInfo.FileLineCol\x1aT\n\x0bTracesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.tensorflow.GraphDebugInfo.StackTrace:\x02\x38\x01\x42\x8c\x01\n\x18org.tensorflow.frameworkB\x14GraphDebugInfoProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.protobuf.graph_debug_info_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\024GraphDebugInfoProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'
  _GRAPHDEBUGINFO_TRACESENTRY._options = None
  _GRAPHDEBUGINFO_TRACESENTRY._serialized_options = b'8\001'
  _GRAPHDEBUGINFO._serialized_start=64
  _GRAPHDEBUGINFO._serialized_end=405
  _GRAPHDEBUGINFO_FILELINECOL._serialized_start=153
  _GRAPHDEBUGINFO_FILELINECOL._serialized_end=241
  _GRAPHDEBUGINFO_STACKTRACE._serialized_start=243
  _GRAPHDEBUGINFO_STACKTRACE._serialized_end=319
  _GRAPHDEBUGINFO_TRACESENTRY._serialized_start=321
  _GRAPHDEBUGINFO_TRACESENTRY._serialized_end=405
# @@protoc_insertion_point(module_scope)
