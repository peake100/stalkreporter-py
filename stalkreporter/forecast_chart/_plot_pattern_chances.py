import matplotlib.pyplot as plt
from gen.stalk_proto import models_pb2 as models
from stalkreporter import colors
from ._consts import LABEL_SIZE
from stalkreporter import utils


PATTERN_NAMES = {
    models.PricePatterns.SMALLSPIKE: "Small Spike",
    models.PricePatterns.BIGSPIKE: "Big Spike",
    models.PricePatterns.DECREASING: "Decreasing",
    models.PricePatterns.FLUCTUATING: "Fluctuating",
}


def plot_pattern_chances(plot: plt.Subplot, forecast: models.Forecast) -> None:
    total = 0.0

    valid_patterns = (x for x in forecast.patterns if x.chance != 0)
    for i, potential_pattern in enumerate(valid_patterns):
        if i > 0:
            # Add a little bit of space between sections
            total += 0.01

        chance = potential_pattern.chance
        # If the chance gets below 2.5%, the bar disappears, so we need to have a
        # minimum visual value for it.
        adjusted_chance = max(potential_pattern.chance, 0.015)

        pattern_color = colors.PATTERN_COLORS[potential_pattern.pattern]

        plot.barh(
            0.5,
            height=0.8,
            width=adjusted_chance,
            left=total,
            color=utils.color(*pattern_color, alpha=chance),
            linewidth=0,
        )

        patten_name = PATTERN_NAMES[potential_pattern.pattern]
        plot.annotate(
            f"{patten_name}: {utils.format_chance(chance)}",
            (total + (adjusted_chance / 2), 0.5),
            color="white",
            alpha=0.75,
            fontsize=LABEL_SIZE * chance ** 0.9 + LABEL_SIZE / 2,
            fontweight="bold",
            ha="center",
            va="center",
        )
        total += adjusted_chance

    plot.set_xlim((0, total))
    plot.set_ylim((0, 1))

    # remove axis labels
    plot.tick_params(
        axis="both",
        labeltop=False,
        labelbottom=False,
        labelright=False,
        labelleft=False,
        top=False,
        bottom=False,
        left=False,
        right=False,
    )

    plot.patch.set_visible(False)
    for spine in plot.spines.values():
        spine.set_visible(False)
