# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thirdparty/kfpbackend/experiment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...thirdparty.kfpbackend import error_pb2 as thirdparty_dot_kfpbackend_dot_error__pb2
from ...thirdparty.kfpbackend import resource_reference_pb2 as thirdparty_dot_kfpbackend_dot_resource__reference__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&thirdparty/kfpbackend/experiment.proto\x12\x15thirdparty.kfpbackend\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!thirdparty/kfpbackend/error.proto\x1a.thirdparty/kfpbackend/resource_reference.proto\"\\\n\x17\x43reateExperimentRequest\x12\x41\n\nexperiment\x18\x01 \x01(\x0b\x32!.thirdparty.kfpbackend.ExperimentR\nexperiment\"&\n\x14GetExperimentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\xdf\x01\n\x16ListExperimentsRequest\x12\x1d\n\npage_token\x18\x01 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x17\n\x07sort_by\x18\x03 \x01(\tR\x06sortBy\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\x12X\n\x16resource_reference_key\x18\x05 \x01(\x0b\x32\".thirdparty.kfpbackend.ResourceKeyR\x14resourceReferenceKey\"\xa5\x01\n\x17ListExperimentsResponse\x12\x43\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32!.thirdparty.kfpbackend.ExperimentR\x0b\x65xperiments\x12\x1d\n\ntotal_size\x18\x03 \x01(\x05R\ttotalSize\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\")\n\x17\x44\x65leteExperimentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\xa2\x03\n\nExperiment\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x39\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12Y\n\x13resource_references\x18\x05 \x03(\x0b\x32(.thirdparty.kfpbackend.ResourceReferenceR\x12resourceReferences\x12S\n\rstorage_state\x18\x06 \x01(\x0e\x32..thirdparty.kfpbackend.Experiment.StorageStateR\x0cstorageState\"c\n\x0cStorageState\x12\x1c\n\x18STORAGESTATE_UNSPECIFIED\x10\x00\x12\x1a\n\x16STORAGESTATE_AVAILABLE\x10\x01\x12\x19\n\x15STORAGESTATE_ARCHIVED\x10\x02\"*\n\x18\x41rchiveExperimentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\",\n\x1aUnarchiveExperimentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id2\xf2\x06\n\x11\x45xperimentService\x12\x94\x01\n\x10\x43reateExperiment\x12..thirdparty.kfpbackend.CreateExperimentRequest\x1a!.thirdparty.kfpbackend.Experiment\"-\x82\xd3\xe4\x93\x02\'\"\x19/apis/v1beta1/experiments:\nexperiment\x12\x87\x01\n\rGetExperiment\x12+.thirdparty.kfpbackend.GetExperimentRequest\x1a!.thirdparty.kfpbackend.Experiment\"&\x82\xd3\xe4\x93\x02 \x12\x1e/apis/v1beta1/experiments/{id}\x12\x92\x01\n\x0eListExperiment\x12-.thirdparty.kfpbackend.ListExperimentsRequest\x1a..thirdparty.kfpbackend.ListExperimentsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/apis/v1beta1/experiments\x12\x82\x01\n\x10\x44\x65leteExperiment\x12..thirdparty.kfpbackend.DeleteExperimentRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02 *\x1e/apis/v1beta1/experiments/{id}\x12\x8c\x01\n\x11\x41rchiveExperiment\x12/.thirdparty.kfpbackend.ArchiveExperimentRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(\"&/apis/v1beta1/experiments/{id}:archive\x12\x92\x01\n\x13UnarchiveExperiment\x12\x31.thirdparty.kfpbackend.UnarchiveExperimentRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02*\"(/apis/v1beta1/experiments/{id}:unarchiveB@Z>github.com/kubeflow/pipelines/backend/api/go_client;kfpbackendb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thirdparty.kfpbackend.experiment_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/kubeflow/pipelines/backend/api/go_client;kfpbackend'
  _EXPERIMENTSERVICE.methods_by_name['CreateExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['CreateExperiment']._serialized_options = b'\202\323\344\223\002\'\"\031/apis/v1beta1/experiments:\nexperiment'
  _EXPERIMENTSERVICE.methods_by_name['GetExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['GetExperiment']._serialized_options = b'\202\323\344\223\002 \022\036/apis/v1beta1/experiments/{id}'
  _EXPERIMENTSERVICE.methods_by_name['ListExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['ListExperiment']._serialized_options = b'\202\323\344\223\002\033\022\031/apis/v1beta1/experiments'
  _EXPERIMENTSERVICE.methods_by_name['DeleteExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['DeleteExperiment']._serialized_options = b'\202\323\344\223\002 *\036/apis/v1beta1/experiments/{id}'
  _EXPERIMENTSERVICE.methods_by_name['ArchiveExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['ArchiveExperiment']._serialized_options = b'\202\323\344\223\002(\"&/apis/v1beta1/experiments/{id}:archive'
  _EXPERIMENTSERVICE.methods_by_name['UnarchiveExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['UnarchiveExperiment']._serialized_options = b'\202\323\344\223\002*\"(/apis/v1beta1/experiments/{id}:unarchive'
  _CREATEEXPERIMENTREQUEST._serialized_start=240
  _CREATEEXPERIMENTREQUEST._serialized_end=332
  _GETEXPERIMENTREQUEST._serialized_start=334
  _GETEXPERIMENTREQUEST._serialized_end=372
  _LISTEXPERIMENTSREQUEST._serialized_start=375
  _LISTEXPERIMENTSREQUEST._serialized_end=598
  _LISTEXPERIMENTSRESPONSE._serialized_start=601
  _LISTEXPERIMENTSRESPONSE._serialized_end=766
  _DELETEEXPERIMENTREQUEST._serialized_start=768
  _DELETEEXPERIMENTREQUEST._serialized_end=809
  _EXPERIMENT._serialized_start=812
  _EXPERIMENT._serialized_end=1230
  _EXPERIMENT_STORAGESTATE._serialized_start=1131
  _EXPERIMENT_STORAGESTATE._serialized_end=1230
  _ARCHIVEEXPERIMENTREQUEST._serialized_start=1232
  _ARCHIVEEXPERIMENTREQUEST._serialized_end=1274
  _UNARCHIVEEXPERIMENTREQUEST._serialized_start=1276
  _UNARCHIVEEXPERIMENTREQUEST._serialized_end=1320
  _EXPERIMENTSERVICE._serialized_start=1323
  _EXPERIMENTSERVICE._serialized_end=2205
# @@protoc_insertion_point(module_scope)
