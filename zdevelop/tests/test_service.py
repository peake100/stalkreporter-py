import pytest
from grpclib.client import Channel
from protogen.stalk_proto import models_pb2 as models
from protogen.stalk_proto import forecaster_grpc as forecaster
from protogen.stalk_proto import reporter_grpc as reporter


@pytest.mark.asyncio
async def test_chart_req(service: None) -> None:
    big_progression = [95, 92, 89, 86, 117, 197]

    channel_forecast = Channel(
        host="stalkforecastergrpc-env.eba-evmzyctu.us-east-2.elasticbeanstalk.com",
        port=50051,
    )
    forecast_client = forecaster.StalkForecasterStub(channel_forecast)

    channel_reports = Channel(host="localhost", port=50051)
    reports_client = reporter.StalkReporterStub(channel_reports)

    ticker = models.Ticker(
        purchase_price=107,
        previous_pattern=models.PricePatterns.UNKNOWN,
        prices=big_progression,
        current_period=len(big_progression) - 1,
    )
    forecast = await forecast_client.ForecastPrices(ticker)

    chart_req = models.ReqForecastChart(
        ticker=ticker, forecast=forecast, format=models.ImageFormat.SVG
    )
    resp = await reports_client.ForecastChart(chart_req)

    assert resp is not None
    assert len(resp.chart) > 100

    channel_forecast.close()
    channel_reports.close()
