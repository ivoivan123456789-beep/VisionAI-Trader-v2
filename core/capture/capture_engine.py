import time
import cv2
import dxcam
import numpy as np
import win32gui

from core.capture.window_finder import find_tradingview_window


class CaptureEngine:
    """
    DXcam capture engine.

    Finds the TradingView window and continuously
    crops it from the monitor capture.
    """

    def __init__(self):

        self.camera = dxcam.create(output_color="BGR")

        self.hwnd = None
        self.title = None

        self.connected = False

    # ---------------------------------------------------------

    def connect(self):

        hwnd, title = find_tradingview_window()

        if hwnd is None:
            self.connected = False
            return False

        self.hwnd = hwnd
        self.title = title

        self.connected = True

        return True

    # ---------------------------------------------------------

    def is_connected(self):

        if self.hwnd is None:
            return False

        return win32gui.IsWindow(self.hwnd)

    # ---------------------------------------------------------

    def capture(self):

        if not self.connected:
            return None

        try:

            if not self.is_connected():
                self.connected = False
                return None

            left, top, right, bottom = win32gui.GetWindowRect(
                self.hwnd
            )

            screen = self.camera.grab()

            if screen is None:
                return None

            h, w = screen.shape[:2]

            left = max(0, left)
            top = max(0, top)

            right = min(w, right)
            bottom = min(h, bottom)

            frame = screen[top:bottom, left:right]

            if frame.size == 0:
                return None

            return frame.copy()

        except Exception as e:

            print("CaptureEngine:", e)

            self.connected = False

            return None

    # ---------------------------------------------------------

    def reconnect(self):

        self.connected = False

        while not self.connected:

            self.connect()

            if self.connected:
                break

            time.sleep(1)