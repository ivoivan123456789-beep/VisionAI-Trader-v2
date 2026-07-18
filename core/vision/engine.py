from core.vision.preprocess import Preprocessor
from core.vision.result import VisionResult


class VisionEngine:
    """
    Main Computer Vision pipeline.

    Every captured TradingView frame passes through here.
    """

    def __init__(self):

        self.preprocessor = Preprocessor()

    # ---------------------------------------------------------

    def process(self, frame):

        result = VisionResult()

        processed = self.preprocessor.process(frame)

        result.original = processed["original"]
        result.chart = processed["chart"]
        result.gray = processed["gray"]
        result.edges = processed["edges"]

        #
        # Future modules
        #
        # result.market = SwingDetector().detect(...)
        # result.market = StructureDetector().detect(...)
        # result.market = LiquidityDetector().detect(...)
        #

        return result