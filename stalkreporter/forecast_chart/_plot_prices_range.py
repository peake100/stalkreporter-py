import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from protogen.stalk_proto import models_pb2 as models
from typing import Optional

from stalkreporter import colors
from ._consts import (
    PRICE_Y_LIM,
    LABEL_SIZE,
)


def _create_price_watermark(
    plot: plt.Subplot,
    name: str,
    price: int,
    va_top: bool,
    pattern: Optional["models.PricePatterns"],
) -> None:
    y_text_offset = 5

    if va_top:
        vertical_alignment = "top"
        y_text_offset *= -1
    else:
        vertical_alignment = "bottom"

    if pattern is None:
        pattern_color = colors.CURRENT_PRICE_COLOR
    else:
        pattern_color = colors.PATTERN_COLORS[pattern]

    # Create a dotted line line at the break-even point that matches the price
    # progression
    price_line = mlines.Line2D(
        [0, 4], [price, price], color=pattern_color, linewidth=2, linestyle="--",
    )
    plot.add_line(price_line)

    plot.annotate(
        f"{name}: {price}",
        (2, price),
        textcoords="offset points",
        xytext=(0, y_text_offset),
        horizontalalignment="center",
        verticalalignment=vertical_alignment,
        color=pattern_color,
        fontsize=LABEL_SIZE,
        bbox={
            "boxstyle": "Circle,pad=0.6",
            "facecolor": colors.color(0, 0, 0, alpha=0.1),
            "edgecolor": "none",
            "linewidth": 0,
        },
    )


def plot_prices_range(
    plot: plt.Subplot, ticker: models.Ticker, forecast: models.Forecast,
) -> None:
    max_pattern = models.PricePatterns.UNKNOWN
    guaranteed_pattern = models.PricePatterns.UNKNOWN
    min_pattern = models.PricePatterns.UNKNOWN

    break_even = ticker.purchase_price

    plot.axes.set_ylim(PRICE_Y_LIM)
    plot.axes.set_xlim([0, 4])

    bar_anchors = np.arange(4)

    for i, potential_pattern in enumerate(forecast.patterns):
        bar_position = bar_anchors[i]

        if len(potential_pattern.potential_weeks) == 0:
            continue

        min_price = potential_pattern.prices_future.min
        max_price = potential_pattern.prices_future.max

        pattern_color = colors.PATTERN_COLORS[potential_pattern.pattern]
        bar_color = colors.color(*pattern_color, alpha=potential_pattern.chance)

        plot.bar(
            [bar_position],
            [max_price - min_price],
            bottom=min_price,
            width=0.4,
            align="edge",
            color=bar_color,
        )

        if potential_pattern.prices_future.max == forecast.prices_future.max:
            max_pattern = potential_pattern.pattern

        if (
            potential_pattern.prices_future.guaranteed
            == forecast.prices_future.guaranteed
        ):
            guaranteed_pattern = potential_pattern.pattern

        if potential_pattern.prices_future.min == forecast.prices_future.min:
            min_pattern = potential_pattern.pattern

    # Create a price grid that matches the price progression
    plot.grid(
        axis="y",
        linestyle="-",
        linewidth=0.5,
        color=colors.PRICE_GRID_COLOR,
        alpha=colors.PRICE_GRID_ALPHA,
    )

    # Create a dotted line line at the breakeven point that matches the price
    # progression
    if break_even != 0:
        _create_price_watermark(
            plot, "break-even", break_even, va_top=False, pattern=None
        )

    # Create a dotted line line at the max profit point
    _create_price_watermark(
        plot,
        "potential",
        forecast.prices_future.max,
        va_top=False,
        pattern=max_pattern,
    )

    # Create a dotted line line at the max guaranteed point
    _create_price_watermark(
        plot,
        "guaranteed",
        forecast.prices_future.guaranteed,
        va_top=True,
        pattern=guaranteed_pattern,
    )

    if forecast.prices_summary.min != forecast.prices_summary.guaranteed:
        # Create a dotted line line at the min price
        _create_price_watermark(
            plot,
            "minimum",
            forecast.prices_future.min,
            va_top=True,
            pattern=min_pattern,
        )

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
    for position, spine in plot.spines.items():
        spine.set_visible(False)
