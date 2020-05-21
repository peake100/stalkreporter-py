# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: stalk_proto/reporter.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client

if typing.TYPE_CHECKING:
    import grpclib.server

import protogen.stalk_proto.google.api.annotations_pb2
import protogen.stalk_proto.models_pb2
import protogen.stalk_proto.reporter_pb2


class StalkReporterBase(abc.ABC):
    @abc.abstractmethod
    async def ForecastChart(
        self,
        stream: "grpclib.server.Stream[protogen.stalk_proto.models_pb2.ReqForecastChart, protogen.stalk_proto.models_pb2.RespChart]",
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/proto.StalkReporter/ForecastChart": grpclib.const.Handler(
                self.ForecastChart,
                grpclib.const.Cardinality.UNARY_UNARY,
                protogen.stalk_proto.models_pb2.ReqForecastChart,
                protogen.stalk_proto.models_pb2.RespChart,
            ),
        }


class StalkReporterStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ForecastChart = grpclib.client.UnaryUnaryMethod(
            channel,
            "/proto.StalkReporter/ForecastChart",
            protogen.stalk_proto.models_pb2.ReqForecastChart,
            protogen.stalk_proto.models_pb2.RespChart,
        )
