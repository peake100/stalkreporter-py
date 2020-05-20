from gen.stalk_proto import models_pb2 as models
from typing import Union, Optional, List


def chance_alpha(chance: float) -> float:
    """
    When the alpha has too amny places some, of the objects render as a grey blob,
    so we are going to truncate precision at two places here.
    """
    return round(chance, 2)


def format_chance(chance: float) -> str:
    """
    Print chance as a whole-integer percent. Anything more precise has needless
    visual noise noisy. Exact percentages could always be looked up in a report.
    """
    chance = int(round(chance * 100, 0))
    if chance == 0:
        return "< 1%"
    return f"{chance}%"


def get_pattern(
    forecast: models.Forecast, pattern: models.PricePatterns
) -> models.PotentialPattern:
    """Get a specific potential pattern from a forecast."""
    for potential_pattern in forecast.patterns:
        if potential_pattern.pattern == pattern:
            return potential_pattern

    raise ValueError(f"could not find match for pattern '{pattern}'")


def color(*channels: Union[int, float], alpha: Optional[float] = None) -> List[float]:
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
