# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61nalysis.proto\x12\x08\x61nalysis\"2\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rarchaic_words\x18\x02 \x03(\t\"\xd3\x01\n\x14TextAnalysisResponse\x12\x17\n\x0f\x61vg_word_length\x18\x01 \x01(\x02\x12\x1b\n\x13\x61vg_sentence_length\x18\x02 \x01(\x02\x12M\n\x10word_frequencies\x18\x03 \x03(\x0b\x32\x33.analysis.TextAnalysisResponse.WordFrequenciesEntry\x1a\x36\n\x14WordFrequenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x32W\n\x0f\x41nalysisService\x12\x44\n\x0b\x41nalyzeText\x12\x15.analysis.TextRequest\x1a\x1e.analysis.TextAnalysisResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analysis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TEXTANALYSISRESPONSE_WORDFREQUENCIESENTRY']._loaded_options = None
  _globals['_TEXTANALYSISRESPONSE_WORDFREQUENCIESENTRY']._serialized_options = b'8\001'
  _globals['_TEXTREQUEST']._serialized_start=28
  _globals['_TEXTREQUEST']._serialized_end=78
  _globals['_TEXTANALYSISRESPONSE']._serialized_start=81
  _globals['_TEXTANALYSISRESPONSE']._serialized_end=292
  _globals['_TEXTANALYSISRESPONSE_WORDFREQUENCIESENTRY']._serialized_start=238
  _globals['_TEXTANALYSISRESPONSE_WORDFREQUENCIESENTRY']._serialized_end=292
  _globals['_ANALYSISSERVICE']._serialized_start=294
  _globals['_ANALYSISSERVICE']._serialized_end=381
# @@protoc_insertion_point(module_scope)
