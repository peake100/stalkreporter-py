import io
import matplotlib.pyplot as plt
from matplotlib import gridspec
from gen.stalk_proto import models_pb2 as models
from gen.stalk_proto import reporter_pb2 as models_reporter

from stalkreporter import colors
from ._plot_pattern_chances import plot_pattern_chances
from ._plot_prices_range import plot_prices_range
from ._plot_periods import plot_price_periods


FORMAT_NAMES = {
    models_reporter.ImageFormat.SVG: "svg",
    models_reporter.ImageFormat.PNG: "png",
}


def create_forecast_chart(
    ticker: models.Ticker,
    forecast: models.Forecast,
    image_format: models_reporter.ImageFormat,
) -> io.BytesIO:
    """Create the potential prices chart"""
    fig = plt.figure(figsize=(18, 12), dpi=100)
    fig.set_facecolor(colors.BACKGROUND_COLOR)
    fig.set_edgecolor(colors.BACKGROUND_COLOR)

    grid = gridspec.GridSpec(
        ncols=2, nrows=2, figure=fig, width_ratios=[4, 1], height_ratios=[1.5, 14]
    )

    pattern_chance_plot = fig.add_subplot(grid[0, 0:])
    plot_pattern_chances(pattern_chance_plot, forecast)

    plot_price_range = fig.add_subplot(grid[1, 1])
    plot_prices_range(plot_price_range, ticker, forecast)

    plot_prices = fig.add_subplot(grid[1, 0])
    plot_price_periods(plot_prices, ticker, forecast)

    buf = io.BytesIO()
    fig.savefig(
        buf,
        format=FORMAT_NAMES[image_format],
        bbox_inches="tight",
        pad_inches=0,
        transparent=True,
    )
    fig.show()

    buf.seek(0)
    return buf
