from protogen.stalk_proto import models_pb2 as models


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
