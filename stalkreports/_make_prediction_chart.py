import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as patches
from matplotlib import gridspec
from gen import proto
from typing import List, Optional, Union

PRICE_PERIOD_COUNT = 12

# Alternating 'AM' 'PM' labels
PRICE_TODS = [["AM", "PM"][i % 2] for i in range(PRICE_PERIOD_COUNT)]
PRICE_DAYS = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
PRICE_PERIODS = [x for x in range(PRICE_PERIOD_COUNT)]

# The y range of price graphs
PRICE_Y_LIM = [0, 701]


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
    forecast: proto.Forecast, pattern: proto.PricePatterns
) -> proto.PotentialPattern:
    """Get a specific potential pattern from a forecast."""
    for potential_pattern in forecast.patterns:
        if potential_pattern.pattern == pattern:
            return potential_pattern


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


# TEXT SIZE CONSTANTS
LABEL_SIZE = 16

# COLOR CONSTANTS
BACKGROUND_COLOR = color(63, 63, 63)
PRICE_LABEL_COLOR = color(100, 200, 100, 0.75)
PRICE_GRID_COLOR = color(74, 109, 77)
CURRENT_PRICE_COLOR = color(206, 165, 88)
DAY_LABEL_COLOR = CURRENT_PRICE_COLOR

BIG_SPIKE_COLOR = color(95, 160, 95)
SMALL_SPIKE_COLOR = color(35, 120, 160)
DECREASING_COLOR = color(160, 95, 95)
FLUCTUATING_COLOR = color(200, 100, 200)

# INDEX OF COLORS ASSOCIATED WITH A SPECIFIC PRICE PATTERN
PATTERN_COLORS = {
    proto.PricePatterns.BIGSPIKE: BIG_SPIKE_COLOR,
    proto.PricePatterns.SMALLSPIKE: SMALL_SPIKE_COLOR,
    proto.PricePatterns.DECREASING: DECREASING_COLOR,
    proto.PricePatterns.FLUCTUATING: FLUCTUATING_COLOR,
}


def create_price_bars(
    plot: plt.Subplot,
    week: proto.PotentialWeek,
    pattern: proto.PricePatterns,
) -> None:
    """Add the price par chart for a specific potential week."""

    max_prices: List[int] = list()
    min_prices: List[int] = list()

    for prices in week.prices:
        max_prices.append(prices.max - prices.min)
        min_prices.append(prices.min)

    # the x locations for the bars
    ind = np.arange(PRICE_PERIOD_COUNT)
    width = 1

    plot.bar(
        ind,
        min_prices,
        width,
        color=(0.0, 0.0, 0.0, 0.0),
        edgecolor="none",
    )

    bar_color = PATTERN_COLORS[pattern]
    bar_color = color(*bar_color, alpha=chance_alpha(week.chance))
    plot.bar(
        ind,
        max_prices,
        width,
        bottom=min_prices,
        color=bar_color
    )


def create_pattern_line(
    price_plot: plt.Subplot,
    spike_breakdown: List[float],
    spike_pattern: proto.PotentialPattern,
    spike_color: List[float],
) -> None:
    """Create a dashed line on the max price for periods with a potential spike"""
    period_highs: List[Optional[float]] = [None for _ in range(PRICE_PERIOD_COUNT + 1)]
    spike_progression: List[bool] = [False for _ in range(PRICE_PERIOD_COUNT)]

    # get highest possible price for each period

    first_period = -1
    last_period = -1

    for week in spike_pattern.potential_weeks:
        for period, prices in enumerate(week.prices):
            if not prices.is_spike:
                continue

            if first_period == -1:
                first_period = period
            last_period = period

            spike_progression[period] = True

            high_price = period_highs[period]

            if high_price is None or prices.max > high_price:
                period_highs[period] = prices.max
                if period == 11:
                    period_highs[period + 1] = prices.max

    price_periods: List[float] = PRICE_PERIODS.copy()
    price_periods.append(11.5)

    first_period_price = period_highs[first_period]
    spike_total_anno_location = (first_period - 0.5 - 0.1, first_period_price)

    price_plot.step(
        price_periods,
        period_highs,
        where="mid",
        linestyle="--",
        linewidth=4,
        dash_capstyle="projecting",
        color=spike_color,
        alpha=max(chance_alpha(spike_pattern.chance), 0.1)
    )
    annotation_values = zip(
        PRICE_PERIODS, period_highs, spike_breakdown[12:], spike_progression
    )

    y_annotation_distance = 10

    for period, price, chance, is_spike in annotation_values:
        if not is_spike:
            continue

        # We need to render the numbers ABOVE the spike patter so that they don't
        # get illegible as the spike placement becomes more certain.

        plt.annotate(
            format_chance(chance),
            (period, price),
            textcoords="offset points",
            xytext=(0, y_annotation_distance),
            ha='center',
            va='bottom',
            fontsize=LABEL_SIZE,
            color=spike_color,
        )

    # Annotate the total chance of this spike
    plt.annotate(
        format_chance(spike_pattern.chance) + "\ntotal",
        spike_total_anno_location,
        ha='right',
        va='center',
        fontsize=LABEL_SIZE,
        color="white",
        alpha=0.75,
        bbox={
            "boxstyle": "Circle,pad=0.6",
            "facecolor": color(*spike_color),
            "edgecolor": spike_color,
            "linewidth": 0,
        }
    )

    # Add a label to the daily chances for clarity
    middle = first_period + (last_period - first_period) / 2
    middle_price = next(p for p in period_highs if p)

    plt.annotate(
        "daily:",
        (middle, middle_price + y_annotation_distance * 2.5),
        textcoords="offset points",
        xytext=(0, y_annotation_distance),
        ha='center',
        va='bottom',
        fontsize=LABEL_SIZE * 1.1,
        color=spike_color,
    )


def create_pattern_chance_chart(plot: plt.Subplot, forecast: proto.Forecast):
    total = 0.0

    for potential_pattern in forecast.patterns:
        if potential_pattern.chance == 0:
            continue

        chance = potential_pattern.chance
        # If the chance gets below 2.5%, the bar disappears, so we need to have a
        # minimum visual value for it.
        adjusted_chance = max(potential_pattern.chance, 0.025)

        pattern_color = PATTERN_COLORS[potential_pattern.pattern]

        plot.barh(
            0.5,
            height=1,
            width=adjusted_chance,
            left=total,
            color=color(*pattern_color, alpha=chance),
            linewidth=10,
            edgecolor=BACKGROUND_COLOR,
        )

        patten_name = proto.PricePatterns(potential_pattern.pattern).name
        plot.annotate(
            f"{patten_name}: {format_chance(chance)}",
            (total + (adjusted_chance / 2), 0.5),
            color="white",
            alpha=0.75,
            fontsize=LABEL_SIZE * chance ** 0.9 + LABEL_SIZE / 2,
            fontweight="bold",
            ha="center",
            va="center"
        )
        total += adjusted_chance

    plot.set_xlim((0, total))
    plot.set_ylim((0, 1))

    # remove axis labels
    plot.tick_params(
        axis='both',
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


def create_weekday_grid(weekday_labels: plt.Subplot,) -> None:
    weekday_labels.grid(
        axis='x', linestyle='-', linewidth=2, color="white", alpha=0.02
    )


def plot_current_prices(plot_prices: plt.Subplot, ticker: proto.Ticker) -> int:
    current_period = -1
    prices = [None for _ in range(0, PRICE_PERIOD_COUNT + 2)]
    prices[0] = ticker.purchase_price

    for i in range(0, PRICE_PERIOD_COUNT):
        try:
            this_price = ticker.prices[i]
        except IndexError:
            continue

        if this_price != 0:
            prices[i + 1] = this_price

            current_period = i

    plot_prices.step(
        [i for i in range(-1, PRICE_PERIOD_COUNT + 1)], prices,
        where="mid",
        linestyle="--",
        linewidth=2,
        dash_capstyle="projecting",
        color=CURRENT_PRICE_COLOR,
    )

    # Create a shaded region for the current period
    rect = patches.Rectangle(
        (current_period - 0.5, 0),
        1,
        701,
        linewidth=0,
        color=CURRENT_PRICE_COLOR,
        alpha=0.1
    )

    # Add the patch to the Axes
    plot_prices.add_patch(rect)

    # Create a line at the head of the current price period
    current_period_line = mlines.Line2D(
        [current_period + 0.5, current_period + 0.5],
        [0, 700],
        color=CURRENT_PRICE_COLOR,
    )
    plot_prices.add_line(current_period_line)

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
            ha='center',
            va='bottom',
            fontsize=LABEL_SIZE,
            color=CURRENT_PRICE_COLOR,
        )

    return current_period


def create_prices_graph(
    plot_prices: plt.Subplot, ticker: proto.Ticker, forecast: proto.Forecast,
) -> None:

    # set bg color for all graphs
    for plot in [plot_prices]:
        plot.set_facecolor(BACKGROUND_COLOR)
        # Remove all spines
        for spine in plot.spines.values():
            spine.set_visible(False)

    plot_prices.set_facecolor(BACKGROUND_COLOR)
    plot_prices.set_ylim(PRICE_Y_LIM)
    plot_prices.axes.set_yticks(np.arange(0, 701, 100))

    plot_prices.grid(axis='y', linestyle='-', linewidth='0.5', color=PRICE_GRID_COLOR)

    for pattern in forecast.patterns:
        for week in pattern.potential_weeks:
            create_price_bars(plot_prices, week, pattern.pattern)

    big_pattern = get_pattern(forecast, proto.PricePatterns.BIGSPIKE)
    if big_pattern.chance > 0:
        create_pattern_line(
            plot_prices,
            spike_breakdown=forecast.spikes.big.breakdown,
            spike_pattern=big_pattern,
            spike_color=BIG_SPIKE_COLOR,
        )

    small_pattern = get_pattern(forecast, proto.PricePatterns.SMALLSPIKE)
    if small_pattern.chance > 0:
        create_pattern_line(
            plot_prices,
            spike_breakdown=forecast.spikes.small.breakdown,
            spike_pattern=small_pattern,
            spike_color=SMALL_SPIKE_COLOR,
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
    weekday_labels.spines["bottom"].set_position(("axes", -0.04))
    create_weekday_grid(weekday_labels)

    # style price axes
    plot_prices.tick_params(
        axis='y',
        labelcolor=PRICE_LABEL_COLOR,
        labelsize=LABEL_SIZE * .85,
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
        axis='x',
        labelcolor=DAY_LABEL_COLOR,
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
        axis='both',
        labelcolor=DAY_LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labelbottom=True,
        labeltop=False,
        bottom=False,
        top=False,
        left=False,
    )

    # Style tod and day label for current price period
    current_period = plot_current_prices(plot_prices, ticker)
    if current_period != -1:
        bbox = dict(
            boxstyle="round,pad=0.5",
            color=DAY_LABEL_COLOR,
        )
        current_tod_label = bottom_axis.xaxis.get_ticklabels()[current_period]
        current_tod_label.set_color("white")
        current_tod_label.set_bbox(bbox)

    all_spines = itertools.chain(
        plot_prices.spines.values(),
        weekday_labels.spines.values(),
    )
    for spine in all_spines:
        spine.set_visible(False)


def create_price_watermark(
    plot: plt.Subplot,
    name: str,
    price: int,
    va_top: bool,
    pattern: Optional[proto.PricePatterns],
) -> None:
    y_text_offset = 5

    if va_top:
        vertical_alignment = "top"
        y_text_offset *= -1
    else:
        vertical_alignment = "bottom"

    pattern_color = PATTERN_COLORS.get(pattern, CURRENT_PRICE_COLOR)

    # Create a dotted line line at the breakeven point that matches the price
    # progression
    price_line = mlines.Line2D(
        [0, 4],
        [price, price],
        color=pattern_color,
        linewidth=2,
        linestyle="--",
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
    )


def create_min_max_chart(
    plot: plt.Subplot, ticker: proto.Ticker, forecast: proto.Forecast,
) -> None:
    max_pattern = proto.PricePatterns.UNKNOWN
    guaranteed_pattern = proto.PricePatterns.UNKNOWN
    min_pattern = proto.PricePatterns.UNKNOWN
    min_price = 1000

    break_even = ticker.purchase_price

    plot.axes.set_ylim(PRICE_Y_LIM)
    plot.axes.set_xlim([0, 4])

    bar_anchors = np.arange(4)

    values: List[int] = list()

    for i, potential_pattern in enumerate(forecast.patterns):
        bar_position = bar_anchors[i]

        if len(potential_pattern.potential_weeks) == 0:
            values.append(0)
            values.append(0)
            continue

        min_price = potential_pattern.prices_summary.min
        max_price = potential_pattern.prices_summary.max

        pattern_color = PATTERN_COLORS[potential_pattern.pattern]
        bar_color = color(*pattern_color, alpha=potential_pattern.chance)

        plot.bar(
            [bar_position],
            [max_price - min_price],
            bottom=min_price,
            width=0.4,
            align='edge',
            color=bar_color,
        )

        if potential_pattern.prices_summary.max == forecast.prices_summary.max:
            max_pattern = proto.PricePatterns(potential_pattern.pattern)

        if potential_pattern.prices_summary.min == forecast.prices_summary.min:
            guaranteed_pattern = proto.PricePatterns(potential_pattern.pattern)

        for week in potential_pattern.potential_weeks:
            for prices in week.prices:
                if prices.min < min_price:
                    min_price = prices.min
                    min_pattern = proto.PricePatterns(potential_pattern.pattern)

    # Create a price grid that matches the price progression
    plot.grid(axis='y', linestyle='-', linewidth='0.5', color=PRICE_GRID_COLOR)

    # Create a dotted line line at the breakeven point that matches the price
    # progression
    create_price_watermark(plot, "break-even", break_even, va_top=False, pattern=None)

    # Create a dotted line line at the max profit point
    create_price_watermark(
        plot,
        "potential",
        forecast.prices_summary.max,
        va_top=False,
        pattern=max_pattern
    )

    # Create a dotted line line at the max guaranteed point
    create_price_watermark(
        plot,
        "guaranteed",
        forecast.prices_summary.min,
        va_top=True,
        pattern=guaranteed_pattern
    )

    if min_price != forecast.prices_summary.min:
        # Create a dotted line line at the min price
        create_price_watermark(
            plot,
            "minimum",
            min_price,
            va_top=True,
            pattern=min_pattern
        )

    # remove axis labels
    plot.tick_params(
        axis='both',
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


def create_prediction_report(ticker: proto.Ticker, forecast: proto.Forecast) -> None:
    """Create the potential prices chart"""
    fig = plt.figure(figsize=(18, 12), dpi=100)
    fig.set_facecolor(BACKGROUND_COLOR)
    fig.set_edgecolor(BACKGROUND_COLOR)

    grid = gridspec.GridSpec(
        ncols=2,
        nrows=2,
        figure=fig,
        width_ratios=[4, 1],
        height_ratios=[1.5, 14]
    )

    pattern_chance_plot = fig.add_subplot(grid[0, 0:])
    create_pattern_chance_chart(pattern_chance_plot, forecast)

    plot_price_range = fig.add_subplot(grid[1, 1])
    create_min_max_chart(plot_price_range, ticker, forecast)

    plot_prices = fig.add_subplot(grid[1, 0])
    create_prices_graph(plot_prices, ticker, forecast)

    plt.show()
