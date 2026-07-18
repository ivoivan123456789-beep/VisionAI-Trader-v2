from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class ChartWidget(QLabel):
    """
    Widget responsible for displaying
    the live TradingView chart.
    """

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumSize(900, 600)

        self.setText("Waiting for TradingView...")

        self.setStyleSheet("""
            QLabel{
                background:#111111;
                color:white;
                border:1px solid #444444;
                font-size:16px;
            }
        """)

        self._pixmap = None

    # ---------------------------------------------------------

    def set_frame(self, image: QImage):

        self._pixmap = QPixmap.fromImage(image)

        self._update_view()

    # ---------------------------------------------------------

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self._update_view()

    # ---------------------------------------------------------

    def _update_view(self):

        if self._pixmap is None:
            return

        scaled = self._pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(scaled)

    # ---------------------------------------------------------

    def clear_chart(self):

        self._pixmap = None

        self.setPixmap(QPixmap())

        self.setText("Waiting for TradingView...")