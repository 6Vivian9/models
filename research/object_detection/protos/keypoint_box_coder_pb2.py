# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/keypoint_box_coder.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'object_detection/protos/keypoint_box_coder.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0object_detection/protos/keypoint_box_coder.proto\x12\x17object_detection.protos\"\x84\x01\n\x10KeypointBoxCoder\x12\x15\n\rnum_keypoints\x18\x01 \x01(\x05\x12\x13\n\x07y_scale\x18\x02 \x01(\x02:\x02\x31\x30\x12\x13\n\x07x_scale\x18\x03 \x01(\x02:\x02\x31\x30\x12\x17\n\x0cheight_scale\x18\x04 \x01(\x02:\x01\x35\x12\x16\n\x0bwidth_scale\x18\x05 \x01(\x02:\x01\x35')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.keypoint_box_coder_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KEYPOINTBOXCODER']._serialized_start=78
  _globals['_KEYPOINTBOXCODER']._serialized_end=210
# @@protoc_insertion_point(module_scope)
