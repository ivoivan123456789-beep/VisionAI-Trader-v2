from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

import cv2

from core.capture.capture_engine import CaptureEngine


class CaptureThread(QThread):
    """
    Background thread that captures TradingView
    and sends frames to the UI.
    """

    frame_ready = Signal(QImage)
    status_changed = Signal(str)
    fps_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.engine = CaptureEngine()

        self.running = False

    # -----------------------------------------------------

    def stop(self):

        self.running = False

        self.wait()

    # -----------------------------------------------------

    def run(self):

        self.running = True

        if not self.engine.connect():

            self.status_changed.emit("TradingView: Offline")
            return

        self.status_changed.emit("TradingView: Connected")

        timer = cv2.TickMeter()

        frames = 0

        while self.running:

            timer.start()

            frame = self.engine.capture()

            if frame is None:

                self.status_changed.emit("TradingView: Reconnecting...")

                self.engine.reconnect()

                self.status_changed.emit("TradingView: Connected")

                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = rgb.shape

            image = QImage(
                rgb.data,
                w,
                h,
                ch * w,
                QImage.Format_RGB888,
            ).copy()

            self.frame_ready.emit(image)

            frames += 1

            timer.stop()

            if timer.getTimeSec() >= 1.0:

                self.fps_changed.emit(frames)

                frames = 0

                timer.reset()

            self.msleep(30)