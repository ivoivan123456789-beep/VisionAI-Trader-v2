from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class SwingPoint:
    x: int
    y: int
    kind: str  # "HH", "HL", "LH", "LL"


@dataclass
class StructureEvent:
    name: str
    start: Tuple[int, int]
    end: Tuple[int, int]


@dataclass
class Zone:
    left: int
    top: int
    right: int
    bottom: int
    zone_type: str


@dataclass
class MarketState:
    """
    Central market model.

    Every detector updates this object.

    The AI only reads this object.
    """

    trend: str = "Unknown"

    confidence: float = 0.0

    current_price: float = 0.0

    swing_highs: List[SwingPoint] = field(default_factory=list)

    swing_lows: List[SwingPoint] = field(default_factory=list)

    bos_events: List[StructureEvent] = field(default_factory=list)

    choch_events: List[StructureEvent] = field(default_factory=list)

    order_blocks: List[Zone] = field(default_factory=list)

    fair_value_gaps: List[Zone] = field(default_factory=list)

    liquidity_zones: List[Zone] = field(default_factory=list)

    # ---------------------------------------------------------

    def clear(self):

        self.swing_highs.clear()
        self.swing_lows.clear()

        self.bos_events.clear()
        self.choch_events.clear()

        self.order_blocks.clear()
        self.fair_value_gaps.clear()
        self.liquidity_zones.clear()

        self.trend = "Unknown"
        self.confidence = 0.0