from dataclasses import dataclass
from typing import Optional

import numpy as np

from core.analysis.market_state import MarketState


@dataclass
class VisionResult:
    """
    Container returned by the Vision Engine.

    Every processing step stores its results here.
    """

    # Original captured frame
    original: Optional[np.ndarray] = None

    # Cropped TradingView chart
    chart: Optional[np.ndarray] = None

    # Grayscale version
    gray: Optional[np.ndarray] = None

    # Edge image
    edges: Optional[np.ndarray] = None

    # AI market model
    market: MarketState = None

    def __post_init__(self):

        if self.market is None:
            self.market = MarketState()

    # ---------------------------------------------------------

    @property
    def width(self):

        if self.chart is None:
            return 0

        return self.chart.shape[1]

    # ---------------------------------------------------------

    @property
    def height(self):

        if self.chart is None:
            return 0

        return self.chart.shape[0]

    # ---------------------------------------------------------

    def clear(self):

        self.original = None
        self.chart = None
        self.gray = None
        self.edges = None

        self.market.clear()