from PySide6.QtCore import QObject, Signal

from core.capture.capture_thread import CaptureThread
from core.vision.engine import VisionEngine


class CaptureService(QObject):
    """
    Connects the capture thread to the Vision Engine
    and exposes processed frames to the UI.
    """

    frame_ready = Signal(object)
    vision_ready = Signal(object)

    status_changed = Signal(str)
    fps_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.thread = CaptureThread()
        self.vision = VisionEngine()

        self.thread.frame_ready.connect(self._process_frame)
        self.thread.status_changed.connect(self.status_changed)
        self.thread.fps_changed.connect(self.fps_changed)

    # ---------------------------------------------------------

    def _process_frame(self, image):
        """
        Receives a frame from the capture thread.

        Currently we forward the image to the UI.

        Later this method will also send the OpenCV frame
        through the AI detectors.
        """

        # Current UI
        self.frame_ready.emit(image)

        # Vision Engine integration will be enabled
        # once CaptureThread emits raw NumPy frames.
        #
        # Example:
        #
        # result = self.vision.process(frame)
        # self.vision_ready.emit(result)

    # ---------------------------------------------------------

    def start(self):

        if not self.thread.isRunning():
            self.thread.start()

    # ---------------------------------------------------------

    def stop(self):

        if self.thread.isRunning():
            self.thread.stop()

    # ---------------------------------------------------------

    def is_running(self):

        return self.thread.isRunning()