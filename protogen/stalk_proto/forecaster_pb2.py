# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stalk_proto/forecaster.proto

from protogen.stalk_proto import models_pb2 as stalk__proto_dot_models__pb2
from protogen.stalk_proto.google.api import (
    annotations_pb2 as stalk__proto_dot_google_dot_api_dot_annotations__pb2,
)
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="stalk_proto/forecaster.proto",
    package="proto",
    syntax="proto3",
    serialized_options=b"Z,github.com/peake100/stalkforecaster-go/proto",
    serialized_pb=b'\n\x1cstalk_proto/forecaster.proto\x12\x05proto\x1a(stalk_proto/google/api/annotations.proto\x1a\x18stalk_proto/models.proto2Y\n\x0fStalkForecaster\x12\x46\n\x0e\x46orecastPrices\x12\r.proto.Ticker\x1a\x0f.proto.Forecast"\x14\x82\xd3\xe4\x93\x02\x0e"\t/forecast:\x01*B.Z,github.com/peake100/stalkforecaster-go/protob\x06proto3',
    dependencies=[
        stalk__proto_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        stalk__proto_dot_models__pb2.DESCRIPTOR,
    ],
)


_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_STALKFORECASTER = _descriptor.ServiceDescriptor(
    name="StalkForecaster",
    full_name="proto.StalkForecaster",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=107,
    serialized_end=196,
    methods=[
        _descriptor.MethodDescriptor(
            name="ForecastPrices",
            full_name="proto.StalkForecaster.ForecastPrices",
            index=0,
            containing_service=None,
            input_type=stalk__proto_dot_models__pb2._TICKER,
            output_type=stalk__proto_dot_models__pb2._FORECAST,
            serialized_options=b'\202\323\344\223\002\016"\t/forecast:\001*',
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_STALKFORECASTER)

DESCRIPTOR.services_by_name["StalkForecaster"] = _STALKFORECASTER

# @@protoc_insertion_point(module_scope)
