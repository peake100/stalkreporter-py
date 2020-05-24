import struct
import codecs
from protogen.stalk_proto import models_pb2 as models
from typing import List, Union, Optional


ColorType = List[float]


def color(*channels: Union[int, float], alpha: Optional[float] = None) -> ColorType:
    """
    Convert a set 0-255 RGB int values to 0.0-1.0 floats. Alpha is expected to already
    be formatted as a float.

    If the ``channels`` values are already floats, no changes will be made.
    """
    values: List[float] = list()
    for channel_value in channels:
        if isinstance(channel_value, int):
            channel_value = float(channel_value) / 255.0
        values.append(channel_value)

    if alpha is not None:
        values.append(alpha)

    return values


def hex2rgb(hex_str: str) -> ColorType:
    hex_str = hex_str.lstrip("#")
    return color(*struct.unpack("BBB", codecs.decode(hex_str.encode(), "hex")))


# COLOR CONSTANTS
BACKGROUND_COLOR = color(255, 255, 255)
PRICE_LABEL_COLOR = color(100, 200, 100, 0.75)
PRICE_GRID_COLOR = color(74, 109, 77)
PRICE_GRID_ALPHA = 0.5
DAY_GRID_COLOR = color(255, 255, 255)
DAY_GRID_ALPHA = 0.02
CURRENT_PRICE_COLOR = color(206, 165, 88)
DAY_LABEL_COLOR = CURRENT_PRICE_COLOR
WHITE_LABEL_COLOR = color(255, 255, 255, alpha=0.75)

BIG_SPIKE_COLOR = color(95, 160, 95)
SMALL_SPIKE_COLOR = color(35, 120, 160)
DECREASING_COLOR = color(160, 95, 95)
FLUCTUATING_COLOR = color(200, 100, 200)

# INDEX OF COLORS ASSOCIATED WITH A SPECIFIC PRICE PATTERN
PATTERN_COLORS = {
    models.PricePatterns.BIGSPIKE: BIG_SPIKE_COLOR,
    models.PricePatterns.SMALLSPIKE: SMALL_SPIKE_COLOR,
    models.PricePatterns.DECREASING: DECREASING_COLOR,
    models.PricePatterns.FLUCTUATING: FLUCTUATING_COLOR,
}
