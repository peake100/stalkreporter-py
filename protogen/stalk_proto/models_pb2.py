# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stalk_proto/models.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="stalk_proto/models.proto",
    package="proto",
    syntax="proto3",
    serialized_options=b"Z,github.com/peake100/stalkforecaster-go/proto",
    serialized_pb=b'\n\x18stalk_proto/models.proto\x12\x05proto"x\n\x06Ticker\x12\x16\n\x0epurchase_price\x18\x01 \x01(\x05\x12.\n\x10previous_pattern\x18\x02 \x01(\x0e\x32\x14.proto.PricePatterns\x12\x0e\n\x06prices\x18\x03 \x03(\x05\x12\x16\n\x0e\x63urrent_period\x18\x04 \x01(\x05"9\n\x0bPricePeriod\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x12\x10\n\x08is_spike\x18\x03 \x01(\x08"\x83\x01\n\rPricesSummary\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x12\x12\n\nguaranteed\x18\x06 \x01(\x05\x12\x13\n\x0bmin_periods\x18\x03 \x03(\x05\x12\x13\n\x0bmax_periods\x18\x04 \x03(\x05\x12\x1a\n\x12guaranteed_periods\x18\x05 \x03(\x05"5\n\nSpikeRange\x12\x0b\n\x03has\x18\x01 \x01(\x08\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05"\xc0\x01\n\rPotentialWeek\x12\x0e\n\x06\x63hance\x18\x01 \x01(\x01\x12"\n\x06prices\x18\x03 \x03(\x0b\x32\x12.proto.PricePeriod\x12,\n\x0eprices_summary\x18\x04 \x01(\x0b\x32\x14.proto.PricesSummary\x12+\n\rprices_future\x18\x06 \x01(\x0b\x32\x14.proto.PricesSummary\x12 \n\x05spike\x18\x05 \x01(\x0b\x32\x11.proto.SpikeRange"\xf5\x01\n\x10PotentialPattern\x12%\n\x07pattern\x18\x01 \x01(\x0e\x32\x14.proto.PricePatterns\x12\x0e\n\x06\x63hance\x18\x02 \x01(\x01\x12,\n\x0eprices_summary\x18\x03 \x01(\x0b\x32\x14.proto.PricesSummary\x12+\n\rprices_future\x18\x06 \x01(\x0b\x32\x14.proto.PricesSummary\x12 \n\x05spike\x18\x04 \x01(\x0b\x32\x11.proto.SpikeRange\x12-\n\x0fpotential_weeks\x18\x05 \x03(\x0b\x32\x14.proto.PotentialWeek"Z\n\x0cSpikeChances\x12\x0b\n\x03has\x18\x01 \x01(\x08\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\x12\x0e\n\x06\x63hance\x18\x04 \x01(\x01\x12\x11\n\tbreakdown\x18\x05 \x03(\x01"x\n\x0e\x46orecastSpikes\x12"\n\x05small\x18\x01 \x01(\x0b\x32\x13.proto.SpikeChances\x12 \n\x03\x62ig\x18\x02 \x01(\x0b\x32\x13.proto.SpikeChances\x12 \n\x03\x61ny\x18\x03 \x01(\x0b\x32\x13.proto.SpikeChances"\xb7\x01\n\x08\x46orecast\x12,\n\x0eprices_summary\x18\x01 \x01(\x0b\x32\x14.proto.PricesSummary\x12+\n\rprices_future\x18\x04 \x01(\x0b\x32\x14.proto.PricesSummary\x12%\n\x06spikes\x18\x02 \x01(\x0b\x32\x15.proto.ForecastSpikes\x12)\n\x08patterns\x18\x03 \x03(\x0b\x32\x17.proto.PotentialPattern"x\n\x10ReqForecastChart\x12\x1d\n\x06ticker\x18\x01 \x01(\x0b\x32\r.proto.Ticker\x12!\n\x08\x66orecast\x18\x02 \x01(\x0b\x32\x0f.proto.Forecast\x12"\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x12.proto.ImageFormat"\x1a\n\tRespChart\x12\r\n\x05\x63hart\x18\x01 \x01(\x0c*[\n\rPricePatterns\x12\x0f\n\x0b\x46LUCTUATING\x10\x00\x12\x0c\n\x08\x42IGSPIKE\x10\x01\x12\x0e\n\nDECREASING\x10\x02\x12\x0e\n\nSMALLSPIKE\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04*\x1f\n\x0bImageFormat\x12\x07\n\x03SVG\x10\x00\x12\x07\n\x03PNG\x10\x01\x42.Z,github.com/peake100/stalkforecaster-go/protob\x06proto3',
)

_PRICEPATTERNS = _descriptor.EnumDescriptor(
    name="PricePatterns",
    full_name="proto.PricePatterns",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="FLUCTUATING", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BIGSPIKE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DECREASING", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SMALLSPIKE", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN", index=4, number=4, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1398,
    serialized_end=1489,
)
_sym_db.RegisterEnumDescriptor(_PRICEPATTERNS)

PricePatterns = enum_type_wrapper.EnumTypeWrapper(_PRICEPATTERNS)
_IMAGEFORMAT = _descriptor.EnumDescriptor(
    name="ImageFormat",
    full_name="proto.ImageFormat",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SVG", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PNG", index=1, number=1, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1491,
    serialized_end=1522,
)
_sym_db.RegisterEnumDescriptor(_IMAGEFORMAT)

ImageFormat = enum_type_wrapper.EnumTypeWrapper(_IMAGEFORMAT)
FLUCTUATING = 0
BIGSPIKE = 1
DECREASING = 2
SMALLSPIKE = 3
UNKNOWN = 4
SVG = 0
PNG = 1


_TICKER = _descriptor.Descriptor(
    name="Ticker",
    full_name="proto.Ticker",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="purchase_price",
            full_name="proto.Ticker.purchase_price",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="previous_pattern",
            full_name="proto.Ticker.previous_pattern",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices",
            full_name="proto.Ticker.prices",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="current_period",
            full_name="proto.Ticker.current_period",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=35,
    serialized_end=155,
)


_PRICEPERIOD = _descriptor.Descriptor(
    name="PricePeriod",
    full_name="proto.PricePeriod",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="min",
            full_name="proto.PricePeriod.min",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max",
            full_name="proto.PricePeriod.max",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_spike",
            full_name="proto.PricePeriod.is_spike",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=157,
    serialized_end=214,
)


_PRICESSUMMARY = _descriptor.Descriptor(
    name="PricesSummary",
    full_name="proto.PricesSummary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="min",
            full_name="proto.PricesSummary.min",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max",
            full_name="proto.PricesSummary.max",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="guaranteed",
            full_name="proto.PricesSummary.guaranteed",
            index=2,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="min_periods",
            full_name="proto.PricesSummary.min_periods",
            index=3,
            number=3,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_periods",
            full_name="proto.PricesSummary.max_periods",
            index=4,
            number=4,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="guaranteed_periods",
            full_name="proto.PricesSummary.guaranteed_periods",
            index=5,
            number=5,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=217,
    serialized_end=348,
)


_SPIKERANGE = _descriptor.Descriptor(
    name="SpikeRange",
    full_name="proto.SpikeRange",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="has",
            full_name="proto.SpikeRange.has",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="start",
            full_name="proto.SpikeRange.start",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="end",
            full_name="proto.SpikeRange.end",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=350,
    serialized_end=403,
)


_POTENTIALWEEK = _descriptor.Descriptor(
    name="PotentialWeek",
    full_name="proto.PotentialWeek",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="chance",
            full_name="proto.PotentialWeek.chance",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices",
            full_name="proto.PotentialWeek.prices",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices_summary",
            full_name="proto.PotentialWeek.prices_summary",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices_future",
            full_name="proto.PotentialWeek.prices_future",
            index=3,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="spike",
            full_name="proto.PotentialWeek.spike",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=406,
    serialized_end=598,
)


_POTENTIALPATTERN = _descriptor.Descriptor(
    name="PotentialPattern",
    full_name="proto.PotentialPattern",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pattern",
            full_name="proto.PotentialPattern.pattern",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="chance",
            full_name="proto.PotentialPattern.chance",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices_summary",
            full_name="proto.PotentialPattern.prices_summary",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices_future",
            full_name="proto.PotentialPattern.prices_future",
            index=3,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="spike",
            full_name="proto.PotentialPattern.spike",
            index=4,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="potential_weeks",
            full_name="proto.PotentialPattern.potential_weeks",
            index=5,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=601,
    serialized_end=846,
)


_SPIKECHANCES = _descriptor.Descriptor(
    name="SpikeChances",
    full_name="proto.SpikeChances",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="has",
            full_name="proto.SpikeChances.has",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="start",
            full_name="proto.SpikeChances.start",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="end",
            full_name="proto.SpikeChances.end",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="chance",
            full_name="proto.SpikeChances.chance",
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="breakdown",
            full_name="proto.SpikeChances.breakdown",
            index=4,
            number=5,
            type=1,
            cpp_type=5,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=848,
    serialized_end=938,
)


_FORECASTSPIKES = _descriptor.Descriptor(
    name="ForecastSpikes",
    full_name="proto.ForecastSpikes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="small",
            full_name="proto.ForecastSpikes.small",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="big",
            full_name="proto.ForecastSpikes.big",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="any",
            full_name="proto.ForecastSpikes.any",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=940,
    serialized_end=1060,
)


_FORECAST = _descriptor.Descriptor(
    name="Forecast",
    full_name="proto.Forecast",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="prices_summary",
            full_name="proto.Forecast.prices_summary",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prices_future",
            full_name="proto.Forecast.prices_future",
            index=1,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="spikes",
            full_name="proto.Forecast.spikes",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="patterns",
            full_name="proto.Forecast.patterns",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1063,
    serialized_end=1246,
)


_REQFORECASTCHART = _descriptor.Descriptor(
    name="ReqForecastChart",
    full_name="proto.ReqForecastChart",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ticker",
            full_name="proto.ReqForecastChart.ticker",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="forecast",
            full_name="proto.ReqForecastChart.forecast",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="format",
            full_name="proto.ReqForecastChart.format",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1248,
    serialized_end=1368,
)


_RESPCHART = _descriptor.Descriptor(
    name="RespChart",
    full_name="proto.RespChart",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="chart",
            full_name="proto.RespChart.chart",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1370,
    serialized_end=1396,
)

_TICKER.fields_by_name["previous_pattern"].enum_type = _PRICEPATTERNS
_POTENTIALWEEK.fields_by_name["prices"].message_type = _PRICEPERIOD
_POTENTIALWEEK.fields_by_name["prices_summary"].message_type = _PRICESSUMMARY
_POTENTIALWEEK.fields_by_name["prices_future"].message_type = _PRICESSUMMARY
_POTENTIALWEEK.fields_by_name["spike"].message_type = _SPIKERANGE
_POTENTIALPATTERN.fields_by_name["pattern"].enum_type = _PRICEPATTERNS
_POTENTIALPATTERN.fields_by_name["prices_summary"].message_type = _PRICESSUMMARY
_POTENTIALPATTERN.fields_by_name["prices_future"].message_type = _PRICESSUMMARY
_POTENTIALPATTERN.fields_by_name["spike"].message_type = _SPIKERANGE
_POTENTIALPATTERN.fields_by_name["potential_weeks"].message_type = _POTENTIALWEEK
_FORECASTSPIKES.fields_by_name["small"].message_type = _SPIKECHANCES
_FORECASTSPIKES.fields_by_name["big"].message_type = _SPIKECHANCES
_FORECASTSPIKES.fields_by_name["any"].message_type = _SPIKECHANCES
_FORECAST.fields_by_name["prices_summary"].message_type = _PRICESSUMMARY
_FORECAST.fields_by_name["prices_future"].message_type = _PRICESSUMMARY
_FORECAST.fields_by_name["spikes"].message_type = _FORECASTSPIKES
_FORECAST.fields_by_name["patterns"].message_type = _POTENTIALPATTERN
_REQFORECASTCHART.fields_by_name["ticker"].message_type = _TICKER
_REQFORECASTCHART.fields_by_name["forecast"].message_type = _FORECAST
_REQFORECASTCHART.fields_by_name["format"].enum_type = _IMAGEFORMAT
DESCRIPTOR.message_types_by_name["Ticker"] = _TICKER
DESCRIPTOR.message_types_by_name["PricePeriod"] = _PRICEPERIOD
DESCRIPTOR.message_types_by_name["PricesSummary"] = _PRICESSUMMARY
DESCRIPTOR.message_types_by_name["SpikeRange"] = _SPIKERANGE
DESCRIPTOR.message_types_by_name["PotentialWeek"] = _POTENTIALWEEK
DESCRIPTOR.message_types_by_name["PotentialPattern"] = _POTENTIALPATTERN
DESCRIPTOR.message_types_by_name["SpikeChances"] = _SPIKECHANCES
DESCRIPTOR.message_types_by_name["ForecastSpikes"] = _FORECASTSPIKES
DESCRIPTOR.message_types_by_name["Forecast"] = _FORECAST
DESCRIPTOR.message_types_by_name["ReqForecastChart"] = _REQFORECASTCHART
DESCRIPTOR.message_types_by_name["RespChart"] = _RESPCHART
DESCRIPTOR.enum_types_by_name["PricePatterns"] = _PRICEPATTERNS
DESCRIPTOR.enum_types_by_name["ImageFormat"] = _IMAGEFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ticker = _reflection.GeneratedProtocolMessageType(
    "Ticker",
    (_message.Message,),
    {
        "DESCRIPTOR": _TICKER,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.Ticker)
    },
)
_sym_db.RegisterMessage(Ticker)

PricePeriod = _reflection.GeneratedProtocolMessageType(
    "PricePeriod",
    (_message.Message,),
    {
        "DESCRIPTOR": _PRICEPERIOD,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.PricePeriod)
    },
)
_sym_db.RegisterMessage(PricePeriod)

PricesSummary = _reflection.GeneratedProtocolMessageType(
    "PricesSummary",
    (_message.Message,),
    {
        "DESCRIPTOR": _PRICESSUMMARY,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.PricesSummary)
    },
)
_sym_db.RegisterMessage(PricesSummary)

SpikeRange = _reflection.GeneratedProtocolMessageType(
    "SpikeRange",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPIKERANGE,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.SpikeRange)
    },
)
_sym_db.RegisterMessage(SpikeRange)

PotentialWeek = _reflection.GeneratedProtocolMessageType(
    "PotentialWeek",
    (_message.Message,),
    {
        "DESCRIPTOR": _POTENTIALWEEK,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.PotentialWeek)
    },
)
_sym_db.RegisterMessage(PotentialWeek)

PotentialPattern = _reflection.GeneratedProtocolMessageType(
    "PotentialPattern",
    (_message.Message,),
    {
        "DESCRIPTOR": _POTENTIALPATTERN,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.PotentialPattern)
    },
)
_sym_db.RegisterMessage(PotentialPattern)

SpikeChances = _reflection.GeneratedProtocolMessageType(
    "SpikeChances",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPIKECHANCES,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.SpikeChances)
    },
)
_sym_db.RegisterMessage(SpikeChances)

ForecastSpikes = _reflection.GeneratedProtocolMessageType(
    "ForecastSpikes",
    (_message.Message,),
    {
        "DESCRIPTOR": _FORECASTSPIKES,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.ForecastSpikes)
    },
)
_sym_db.RegisterMessage(ForecastSpikes)

Forecast = _reflection.GeneratedProtocolMessageType(
    "Forecast",
    (_message.Message,),
    {
        "DESCRIPTOR": _FORECAST,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.Forecast)
    },
)
_sym_db.RegisterMessage(Forecast)

ReqForecastChart = _reflection.GeneratedProtocolMessageType(
    "ReqForecastChart",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQFORECASTCHART,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.ReqForecastChart)
    },
)
_sym_db.RegisterMessage(ReqForecastChart)

RespChart = _reflection.GeneratedProtocolMessageType(
    "RespChart",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPCHART,
        "__module__": "stalk_proto.models_pb2"
        # @@protoc_insertion_point(class_scope:proto.RespChart)
    },
)
_sym_db.RegisterMessage(RespChart)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
