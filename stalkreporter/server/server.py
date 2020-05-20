import asyncio
from grpclib import server
from grpclib import utils
from dataclasses import dataclass, field
from gen.stalk_proto import reporter_pb2 as models_reporter
from gen.stalk_proto.reporter_grpc import StalkReporterBase
from gen.stalk_proto.reporter_pb2 import ForecastChartReq, ChartResp
from concurrent.futures import ProcessPoolExecutor

from stalkreporter.forecast_chart import create_forecast_chart


@dataclass
class Resources:
    """Holds common resources the reporting service handlers."""

    # Creating the charts is a cpu-intensive process that takes a second or two to
    # complete. If we ran it directly in our async handlers, we would block the service
    # from taking any incoming requests while a chart was being generated.
    #
    # Secondly, matplotlib is a stateful package, and we would normally
    # need to manage the figure id number for each figure being drawn if we were to
    # handle it in a threading manner, always making sure that one thread is not
    # accidentally working on the figure of another thread.
    #
    # We can sidestep all these problems by running the charting function in a process
    # pool executor, started up before matplotlib is called on to make a figure.
    render_pool: ProcessPoolExecutor = field(init=False)

    def __post_init__(self) -> None:
        self.render_pool = ProcessPoolExecutor()

    async def shutdown(self) -> None:
        self.render_pool.shutdown(wait=True)


def run_forecast(proto_serialized: bytes) -> bytes:
    """
    The generated proto classes are not pickle-able so we need to send them to the
    process pool as raw proto messages and deserialize them there. This function is
    meant to be the target of the process pool and handles receiving the proto message
    from the main process and sending back the rendered chart.
    """
    req = models_reporter.ForecastChartReq.FromString(proto_serialized,)

    svg_buffer = create_forecast_chart(
        ticker=req.ticker, forecast=req.forecast, image_format=req.format,
    )
    return svg_buffer.read()


class StalkReporter(StalkReporterBase):
    def __init__(self, resources: Resources):
        self.resources: Resources = resources
        self.loop = asyncio.get_event_loop()
        super().__init__()

    async def ForecastChart(
        self, stream: server.Stream[ForecastChartReq, ChartResp]
    ) -> None:
        req: models_reporter.ForecastChartReq = await stream.recv_message()
        image_bytes = await self.loop.run_in_executor(
            self.resources.render_pool, run_forecast, req.SerializeToString(),
        )

        resp = ChartResp(chart=image_bytes)
        await stream.send_message(resp)


async def serve() -> None:

    resources = Resources()
    service = server.Server([StalkReporter(resources)])

    with utils.graceful_exit([service]):
        await service.start("localhost", 50051)
        await service.wait_closed()

    await resources.shutdown()
