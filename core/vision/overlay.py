import cv2
import numpy as np


class Overlay:
    """
    Draws AI overlays on top of a chart image.
    """

    def __init__(self):
        self.items = []

    def clear(self):
        self.items.clear()

    def line(self, p1, p2, color=(0, 255, 0), thickness=2):
        self.items.append(("line", p1, p2, color, thickness))

    def rectangle(self, p1, p2, color=(255, 0, 0), thickness=2):
        self.items.append(("rect", p1, p2, color, thickness))

    def circle(self, center, radius=5, color=(0, 0, 255)):
        self.items.append(("circle", center, radius, color))

    def text(self, text, pos, color=(255, 255, 255)):
        self.items.append(("text", text, pos, color))

    def draw(self, frame):

        image = frame.copy()

        for item in self.items:

            kind = item[0]

            if kind == "line":
                _, p1, p2, color, thick = item
                cv2.line(image, p1, p2, color, thick)

            elif kind == "rect":
                _, p1, p2, color, thick = item
                cv2.rectangle(image, p1, p2, color, thick)

            elif kind == "circle":
                _, center, radius, color = item
                cv2.circle(image, center, radius, color, -1)

            elif kind == "text":
                _, txt, pos, color = item
                cv2.putText(
                    image,
                    txt,
                    pos,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    color,
                    2,
                    cv2.LINE_AA,
                )

        return image