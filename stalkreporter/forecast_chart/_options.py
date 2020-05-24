import dataclasses
from typing import Optional

from protogen.stalk_proto import models_pb2 as proto
from stalkreporter import colors


@dataclasses.dataclass
class ForecastOptions:
    ticker: proto.Ticker
    forecast: proto.Forecast
    image_format: proto.ImageFormat
    bg_color: Optional[colors.ColorType]
    debug: bool
