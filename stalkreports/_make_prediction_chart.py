import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from gen import proto
from typing import List, Optional

PRICE_PERIOD_COUNT = 12

# Alternating 'AM' 'PM' labels
PRICE_TODS = [["AM", "PM"][i % 2] for i in range(PRICE_PERIOD_COUNT)]
PRICE_DAYS = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
PRICE_PERIODS = [x for x in range(PRICE_PERIOD_COUNT)]


def get_pattern(
    forecast: proto.Forecast, pattern: proto.PricePatterns
) -> proto.PotentialPattern:
    for potential_pattern in forecast.patterns:
        if potential_pattern.pattern == pattern:
            return potential_pattern


def color(*channels: int, alpha: Optional[float] = None) -> List[float]:
    values = [float(c) / 255.0 for c in channels]
    if alpha is not None:
        values.append(alpha)
    return values


LABEL_SIZE = 16
BACKGROUND_COLOR = color(63, 63, 63)
LABEL_COLOR = color(230, 193, 90)
PRICE_BAR_COLOR = (47, 250, 66)
PRICE_GRID_COLOR = color(74, 109, 77)
BIG_SPIKE_COLOR = color(255, 47, 66)
SMALL_SPIKE_COLOR = color(66, 47, 255)


def bar_color(chance: float) -> List[float]:
    return color(*PRICE_BAR_COLOR, alpha=chance)


def create_price_bars(plot: plt.Subplot, week: proto.PotentialWeek) -> None:
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
    plot.bar(
        ind,
        max_prices,
        width,
        bottom=min_prices,
        color=bar_color(week.chance)
    )


def create_spike_bar(
    spike_plot: plt.Subplot,
    spike_breakdown: List[float],
    spike_color: List[float],
) -> None:
    print(spike_breakdown)
    spike_values: List[int] = list()
    for spike_chance in spike_breakdown:
        if spike_chance:
            spike_values.append(1)
        else:
            spike_values.append(0)

    ind = np.arange(PRICE_PERIOD_COUNT)
    width = 1

    spike_plot.set_ylim([0, 1])

    spike_plot.bar(
        ind,
        spike_values[12:],
        width,
        color=spike_color,
        edgecolor="none",
    )


def create_spike_line(
    price_plot: plt.Subplot,
    spike_breakdown: List[float],
    spike_pattern: proto.PotentialPattern,
    spike_color: List[float],
) -> None:
    period_highs: List[Optional[int]] = [None for _ in range(PRICE_PERIOD_COUNT)]
    # get highest possible price for each period
    for week in spike_pattern.potential_weeks:
        for period, prices in enumerate(week.prices):
            high_price = period_highs[period]
            if (high_price is None or prices.max > high_price) and prices.is_spike:
                period_highs[period] = prices.max

    price_plot.step(
        PRICE_PERIODS,
        period_highs,
        where="mid",
        linestyle="--",
        linewidth=4,
        dash_capstyle="projecting",
    )

    for period, price, chance in zip(PRICE_PERIODS, period_highs, spike_breakdown):
        if price is None:
            continue
        chance = round(chance * 100, 2)

        plt.annotate(
            f"{chance}%",  # this is the text
            (period, price),  # this is the point to label
            textcoords="offset points",  # how to position the text
            xytext=(0, 0),  # distance from text to points (x,y)
            ha='center'
        )


def create_prediction_chart(forecast: proto.Forecast) -> None:
    fig = plt.figure(figsize=(16, 8), dpi=160)

    grid = gridspec.GridSpec(
        ncols=1,
        nrows=3,
        figure=fig,
        height_ratios=[16, 1, 1],
        hspace=0.0
    )

    plot_prices = fig.add_subplot(grid[0])
    plot_big_spike = fig.add_subplot(grid[1])
    plot_small_spike = fig.add_subplot(grid[2])

    fig.set_facecolor(BACKGROUND_COLOR)
    fig.set_edgecolor(BACKGROUND_COLOR)

    # set bg color for all graphs
    for plot in (plot_prices, plot_big_spike, plot_small_spike):
        plot.set_facecolor(BACKGROUND_COLOR)
        # Remove all spines
        for spine in plot.spines.values():
            spine.set_visible(False)

    plot_prices.set_facecolor(BACKGROUND_COLOR)
    plot_prices.set_ylim([0, 701])
    plot_prices.axes.set_yticks(np.arange(0, 701, 100))

    plot_prices.grid(axis='y', linestyle='-', linewidth='0.5', color=PRICE_GRID_COLOR)

    for pattern in forecast.patterns:
        for week in pattern.potential_weeks:
            create_price_bars(plot_prices, week)

    create_spike_bar(plot_big_spike, forecast.spikes.big.breakdown, BIG_SPIKE_COLOR)
    create_spike_line(
        plot_prices,
        spike_breakdown=forecast.spikes.big.breakdown,
        spike_pattern=get_pattern(forecast, proto.PricePatterns.BIGSPIKE),
        spike_color=BIG_SPIKE_COLOR,
    )

    create_spike_bar(
        plot_small_spike, forecast.spikes.small.breakdown, SMALL_SPIKE_COLOR
    )
    create_spike_line(
        plot_prices,
        spike_breakdown=forecast.spikes.small.breakdown,
        spike_pattern=get_pattern(forecast, proto.PricePatterns.SMALLSPIKE),
        spike_color=SMALL_SPIKE_COLOR,
    )

    bottom_axis = plot_small_spike.axes
    # the x locations for the bars
    indTods = np.arange(PRICE_PERIOD_COUNT)
    # Add the time of day labels for each bar
    bottom_axis.axes.set_xlim(plot_prices.get_xlim())
    bottom_axis.axes.set_xticks(indTods)
    bottom_axis.axes.set_xticklabels(PRICE_TODS)
    bottom_axis.spines["bottom"].set_position(("axes", -0.2))

    # Create weekday labels
    weekday_labels = bottom_axis.twiny()
    # We need to make sure the limits match to line up with the bars
    weekday_labels.set_xlim(plot_prices.get_xlim())
    # Place the weekdays between the AM / PM values
    weekday_labels.set_xticks([0.5, 2.5, 4.5, 6.5, 8.5, 10.5])
    # Set the labels
    weekday_labels.set_xticklabels(PRICE_DAYS)
    # Move the weekday labels down a littls
    weekday_labels.spines["bottom"].set_position(("axes", -0.9))

    # style price axes
    plot_prices.tick_params(
        axis='both',
        labelcolor=LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labeltop=False,
        labelbottom=False,
        labelright=True,
        labelleft=True,
        bottom=False,
        top=False,
        left=False,
    )

    # remove big spike axes
    plot_big_spike.tick_params(
        axis='both',
        labeltop=False,
        labelbottom=False,
        labelright=False,
        labelleft=False,
        bottom=False,
        top=False,
        left=False,
        right=False,
    )

    # style TOD labels
    bottom_axis.tick_params(
        axis='both',
        labelcolor=LABEL_COLOR,
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
        labelcolor=LABEL_COLOR,
        labelsize=LABEL_SIZE,
        labelbottom=True,
        labeltop=False,
        bottom=False,
        top=False,
        left=False,
    )

    for spine in itertools.chain(plot_prices.spines.values(), weekday_labels.spines.values()):
        spine.set_visible(False)

    plt.show()
