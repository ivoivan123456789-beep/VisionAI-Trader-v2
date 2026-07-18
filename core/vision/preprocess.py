import cv2
import numpy as np


class Preprocessor:
    """
    Prepares captured TradingView frames for
    computer vision algorithms.
    """

    def __init__(self):

        # Crop values
        # These will become configurable later.
        self.crop_top = 70
        self.crop_bottom = 35
        self.crop_left = 55
        self.crop_right = 260

        self.resize_width = 1280

    # ---------------------------------------------------------

    def crop(self, frame):

        h, w = frame.shape[:2]

        return frame[
            self.crop_top:h - self.crop_bottom,
            self.crop_left:w - self.crop_right
        ]

    # ---------------------------------------------------------

    def resize(self, frame):

        h, w = frame.shape[:2]

        scale = self.resize_width / w

        new_height = int(h * scale)

        return cv2.resize(
            frame,
            (self.resize_width, new_height),
            interpolation=cv2.INTER_AREA
        )

    # ---------------------------------------------------------

    def grayscale(self, frame):

        return cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

    # ---------------------------------------------------------

    def blur(self, gray):

        return cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

    # ---------------------------------------------------------

    def edges(self, gray):

        return cv2.Canny(
            gray,
            60,
            160
        )

    # ---------------------------------------------------------

    def process(self, frame):

        chart = self.crop(frame)

        chart = self.resize(chart)

        gray = self.grayscale(chart)

        blur = self.blur(gray)

        edge = self.edges(blur)

        return {
            "original": frame,
            "chart": chart,
            "gray": gray,
            "edges": edge
        }