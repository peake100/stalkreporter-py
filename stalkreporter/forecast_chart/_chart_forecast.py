import io
import matplotlib.pyplot as plt
from matplotlib import gridspec
from protogen.stalk_proto import models_pb2 as models
from typing import Dict, Any

from ._plot_pattern_chances import plot_pattern_chances
from ._plot_prices_range import plot_prices_range
from ._plot_periods import plot_price_periods
from ._options import ForecastOptions


FORMAT_NAMES = {
    models.ImageFormat.SVG: "svg",
    models.ImageFormat.PNG: "png",
}


def create_forecast_chart(options: ForecastOptions) -> io.BytesIO:
    """Create the potential prices chart"""
    fig = plt.figure(figsize=(18, 12), dpi=70)
    if options.bg_color:
        fig.set_facecolor(options.bg_color)
        fig.set_edgecolor(options.bg_color)

    grid = gridspec.GridSpec(
        ncols=2, nrows=2, figure=fig, width_ratios=[4, 1], height_ratios=[1.5, 14],
    )

    pattern_chance_plot = fig.add_subplot(grid[0, 0:])
    plot_pattern_chances(pattern_chance_plot, options.forecast)

    plot_price_range = fig.add_subplot(grid[1, 1])
    plot_prices_range(plot_price_range, options.ticker, options.forecast)

    plot_prices = fig.add_subplot(grid[1, 0])
    plot_price_periods(plot_prices, options)

    buf = io.BytesIO()
    # Apply padding
    fig.tight_layout(
        rect=[
            options.padding,
            options.padding,
            1 - options.padding,
            1 - options.padding,
        ]
    )

    if not options.bg_color:
        save_kwargs: Dict[str, Any] = dict(transparent=True)
    else:
        save_kwargs = dict(
            facecolor=options.bg_color, edgecolor=options.bg_color, transparent=False,
        )

    fig.savefig(
        buf, format=FORMAT_NAMES[options.image_format], dpi=fig.dpi, **save_kwargs
    )
    if options.debug:
        print("showing figure")
        fig.show()

    fig.clear()
    plt.close(fig)

    buf.seek(0)

    return buf
