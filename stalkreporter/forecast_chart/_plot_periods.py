import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as patches
from protogen.stalk_proto import models_pb2 as models
from typing import List, Optional

from stalkreporter import utils, colors
from ._options import ForecastOptions
from ._consts import (
    PRICE_PERIOD_COUNT,
    PRICE_TODS,
    PRICE_DAYS,
    PRICE_Y_LIM,
    LABEL_SIZE,
    PRICE_PERIODS,
)

# Because of the way we are rendering the step graph, we need to extend it half a period
# on other side so the first and last price period don't take up only half of their
# allotted space
PRICE_PERIODS_EXTENDED: List[float] = [p for p in PRICE_PERIODS]
PRICE_PERIODS_EXTENDED.insert(0, -0.5)
PRICE_PERIODS_EXTENDED.append(11.5)


def _create_week_area(
    plot: plt.Subplot, week: models.PotentialWeek, pattern: models.PricePatterns,
) -> None:
    """Add the price par chart for a specific potential week."""

    min_prices: List[int] = list()
    max_prices: List[int] = list()

    for prices in week.prices:
        min_prices.append(prices.min)
        max_prices.append(prices.max)

    # We need to double up the first and last point so areas for the first and last
    # period hit the edge of the graph
    min_prices.insert(0, min_prices[0])
    max_prices.insert(0, max_prices[0])

    min_prices.append(min_prices[-1])
    max_prices.append(max_prices[-1])

    # the x locations for the bars
    price_color = colors.PATTERN_COLORS[pattern]
    price_color = colors.color(*price_color, alpha=utils.chance_alpha(week.chance))
    plot.fill_between(
        PRICE_PERIODS_EXTENDED,
        min_prices,
        max_prices,
        step="mid",
        facecolor=price_color,
        linewidth=0,
        edgecolor="none",
    )


def _create_pattern_line(
    price_plot: plt.Subplot,
    spike_breakdown: List[float],
    spike_pattern: models.PotentialPattern,
    spike_color: List[float],
) -> None:
    """Create a dashed line on the max price for periods with a potential spike"""
    # get highest possible price for each period

    first_period = spike_pattern.spike.start
    last_period = spike_pattern.spike.end
    high_price = spike_pattern.prices_summary.max

    period_highs: List[Optional[int]] = [
        high_price for _ in range(first_period, last_period + 1)
    ]
    price_periods: List[float] = [p for p in range(first_period, last_period + 1)]

    # Instead of using a plot, we are just going to draw the line directly.
    # Create a line at the head of the current price period
    current_period_line = mlines.Line2D(
        [first_period - 0.5, last_period + 0.5],
        [high_price, high_price],
        color=spike_color,
        linestyle="--",
        linewidth=4,
        # We want this line to be always visible so our alpha floor is going to be .1
        alpha=max(utils.chance_alpha(spike_pattern.chance), 0.1),
    )
    price_plot.add_line(current_period_line)

    y_annotation_distance = 10

    for period in price_periods:
        if period == 11.5:
            continue

        try:
            chance = spike_breakdown[int(period)]
        except TypeError:
            # If this is period '11.5', then we don't need to annotate it, that value
            # is just here for line continuation
            continue

        # We need to render the numbers ABOVE the spike patter so that they don't
        # get illegible as the spike placement becomes more certain.
        price_plot.annotate(
            utils.format_chance(chance),
            (period, high_price),
            textcoords="offset points",
            xytext=(0, y_annotation_distance),
            ha="center",
            va="bottom",
            fontsize=LABEL_SIZE,
            color=spike_color,
        )

    # Annotate the total chance of this spike
    price_plot.annotate(
        utils.format_chance(spike_pattern.chance),
        (first_period - 0.5 - 0.1, high_price),
        ha="right",
        va="center",
        fontsize=LABEL_SIZE,
        color="white",
        alpha=0.75,
        bbox={
            "boxstyle": "Circle,pad=0.6",
            "facecolor": colors.color(*spike_color),
            "edgecolor": spike_color,
            "linewidth": 0,
        },
    )

    # Add a label to the daily chances for clarity
    middle = first_period + (last_period - first_period) / 2
    middle_price = next(p for p in period_highs if p)

    price_plot.annotate(
        "daily:",
        (middle, middle_price + y_annotation_distance * 2.5),
        textcoords="offset points",
        xytext=(0, y_annotation_distance),
        ha="center",
        va="bottom",
        fontsize=LABEL_SIZE * 1.1,
        color=spike_color,
    )


def _create_weekday_grid(weekday_labels: plt.Subplot,) -> None:
    weekday_labels.grid(
        axis="x",
        linestyle="-",
        linewidth=2,
        color=colors.DAY_GRID_COLOR,
        alpha=colors.DAY_GRID_ALPHA,
        zorder=1,
    )


def _plot_current_prices(plot_prices: plt.Subplot, ticker: models.Ticker) -> int:
    current_period = -1
    prices: List[Optional[int]] = [None for _ in range(0, PRICE_PERIOD_COUNT + 2)]
    if ticker.purchase_price != 0:
        prices[0] = ticker.purchase_price

    for i in range(0, PRICE_PERIOD_COUNT):
        try:
            this_price = ticker.prices[i]
        except IndexError:
            continue

        if this_price != 0:
            prices[i + 1] = this_price

            current_period = i

    if ticker.current_period > current_period:
        current_period = ticker.current_period

    plot_prices.step(
        [i for i in range(-1, PRICE_PERIOD_COUNT + 1)],
        prices,
        where="mid",
        linestyle="--",
        linewidth=4,
        dash_capstyle="projecting",
        color=colors.CURRENT_PRICE_COLOR,
    )

    # Annotate the prices
    for i, this_price in enumerate(ticker.prices):
        # Zero means unknown, skip it.
        if this_price == 0:
            continue

        plot_prices.annotate(
            str(this_price),
            (i, this_price),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            va="bottom",
            fontsize=LABEL_SIZE * 1.2,
            color=colors.CURRENT_PRICE_COLOR,
        )

    return current_period


def _add_cursor(plot_prices: plt.Subplot, current_period: int) -> None:
    # Create a shaded region for the current period
    rect = patches.Rectangle(
        (current_period - 0.5, 0),
        1,
        701,
        linewidth=0,
        color=colors.CURRENT_PRICE_COLOR,
        alpha=0.1,
    )

    # Add the patch to the Axes
    plot_prices.add_patch(rect)

    # Create a line at the head of the current price period
    current_period_line = mlines.Line2D(
        [current_period - 0.5, current_period - 0.5],
        [0, 700],
        color=colors.CURRENT_PRICE_COLOR,
    )
    plot_prices.add_line(current_period_line)


def plot_price_periods(plot_prices: plt.Subplot, options: ForecastOptions,) -> None:

    # set bg color for all graphs
    for plot in [plot_prices]:
        plot.set_facecolor(options.bg_color)
        # Remove all spines
        for spine in plot.spines.values():
            spine.set_visible(False)

    plot_prices.set_facecolor(options.bg_color)
    plot_prices.set_ylim(PRICE_Y_LIM)
    plot_prices.set_xlim([-1, 12])
    plot_prices.axes.set_yticks(np.arange(0, 701, 100))

    plot_prices.grid(
        axis="y",
        linestyle="-",
        linewidth=0.5,
        color=colors.PRICE_GRID_COLOR,
        alpha=colors.PRICE_GRID_ALPHA,
    )

    forecast = options.forecast
    for pattern in forecast.patterns:
        for week in pattern.potential_weeks:
            _create_week_area(plot_prices, week, pattern.pattern)

    big_pattern = utils.get_pattern(forecast, models.PricePatterns.BIGSPIKE)
    if big_pattern.chance > 0:
        _create_pattern_line(
            plot_prices,
            spike_breakdown=[x for x in forecast.spikes.big.breakdown],
            spike_pattern=big_pattern,
            spike_color=colors.BIG_SPIKE_COLOR,
        )

    small_pattern = utils.get_pattern(forecast, models.PricePatterns.SMALLSPIKE)
    if small_pattern.chance > 0:
        _create_pattern_line(
            plot_prices,
            spike_breakdown=[x for x in forecast.spikes.small.breakdown],
            spike_pattern=small_pattern,
            spike_color=colors.SMALL_SPIKE_COLOR,
        )

    bottom_axis = plot_prices.axes
    # the x locations for the bars
    indTods = np.arange(PRICE_PERIOD_COUNT)
    # Add the time of day labels for each bar
    bottom_axis.axes.set_xlim(plot_prices.get_xlim())
    bottom_axis.axes.set_xticks(indTods)
    bottom_axis.axes.set_xticklabels(PRICE_TODS)
    bottom_axis.spines["bottom"].set_position(("axes", -0.01))

    # Create weekday labels
    weekday_labels = bottom_axis.twiny()
    # We need to make sure the limits match to line up with the bars
    weekday_labels.set_xlim(plot_prices.get_xlim())
    # Place the weekdays between the AM / PM values
    weekday_labels.set_xticks([0.5, 2.5, 4.5, 6.5, 8.5, 10.5])
    # Set the labels
    weekday_labels.set_xticklabels(PRICE_DAYS)
    # Move the weekday labels down a littls
    weekday_labels.spines["bottom"].set_position(("axes", -0.06))
    _create_weekday_grid(weekday_labels)

    # style price axes
    plot_prices.tick_params(
        axis="y",
        labelcolor=colors.PRICE_LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labeltop=False,
        labelbottom=False,
        labelright=True,
        labelleft=True,
        bottom=False,
        top=False,
        left=False,
    )

    # style TOD labels
    bottom_axis.tick_params(
        axis="x",
        labelcolor=colors.DAY_LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labeltop=False,
        labelbottom=True,
        labelright=False,
        labelleft=False,
        bottom=False,
        top=False,
        left=False,
    )

    # style weekday labels
    weekday_labels.tick_params(
        axis="both",
        labelcolor=colors.DAY_LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labelbottom=True,
        labeltop=False,
        bottom=False,
        top=False,
        left=False,
    )

    # Style tod and day label for current price period
    current_period = _plot_current_prices(plot_prices, options.ticker)
    if current_period != -1:
        bbox = dict(boxstyle="round,pad=0.5", color=colors.DAY_LABEL_COLOR,)
        current_tod_label = bottom_axis.xaxis.get_ticklabels()[current_period]
        current_tod_label.set_color("white")
        current_tod_label.set_bbox(bbox)

    _add_cursor(plot_prices, current_period)

    all_spines = itertools.chain(
        plot_prices.spines.values(), weekday_labels.spines.values(),
    )
    for spine in all_spines:
        spine.set_visible(False)
