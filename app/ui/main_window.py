from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QDockWidget,
    QMainWindow,
    QTextEdit,
    QToolBar,
)

from app.widgets.chart_widget import ChartWidget
from app.services.capture_service import CaptureService


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VisionAI Trader v2")
        self.resize(1600, 900)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()
        self.create_docks()

        # ----------------------------
        # Capture
        # ----------------------------

        self.capture = CaptureService()

        self.capture.frame_ready.connect(
            self.chart_widget.set_frame
        )

        self.capture.status_changed.connect(
            self.tv_status.setText
        )

        self.capture.fps_changed.connect(
            self.update_fps
        )

        self.capture.start()

    # ---------------------------------------------------------

    def closeEvent(self, event):

        self.capture.stop()

        event.accept()

    # ---------------------------------------------------------

    def update_fps(self, fps):

        self.fps_status.setText(f"FPS: {fps}")

    # ---------------------------------------------------------

    def create_menu(self):

        menu = self.menuBar()

        menu.addMenu("File")
        menu.addMenu("View")
        menu.addMenu("Trading")
        menu.addMenu("AI")
        menu.addMenu("Tools")
        menu.addMenu("Help")

    # ---------------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar("Toolbar")

        self.addToolBar(toolbar)

        toolbar.addAction("Connect")
        toolbar.addAction("Analyze")
        toolbar.addAction("Settings")

    # ---------------------------------------------------------

    def create_statusbar(self):

        status = self.statusBar()

        self.tv_status = QLabel("TradingView: Offline")
        self.fps_status = QLabel("FPS: 0")
        self.ai_status = QLabel("AI: Idle")

        status.addPermanentWidget(self.tv_status)
        status.addPermanentWidget(self.fps_status)
        status.addPermanentWidget(self.ai_status)

    # ---------------------------------------------------------

    def create_docks(self):

        chart = QDockWidget("Live Chart", self)

        self.chart_widget = ChartWidget()

        chart.setWidget(self.chart_widget)

        self.addDockWidget(Qt.LeftDockWidgetArea, chart)

        # -------------------------

        analysis = QDockWidget("AI Analysis", self)

        self.analysis = QTextEdit()

        self.analysis.setReadOnly(True)

        self.analysis.setPlainText(
            "Waiting for AI..."
        )

        analysis.setWidget(self.analysis)

        self.addDockWidget(Qt.RightDockWidgetArea, analysis)

        # -------------------------

        signals = QDockWidget("Signals", self)

        self.signals = QTextEdit()

        self.signals.setReadOnly(True)

        signals.setWidget(self.signals)

        self.addDockWidget(Qt.BottomDockWidgetArea, signals)

        # -------------------------

        log = QDockWidget("Log", self)

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.append("VisionAI Trader started.")

        log.setWidget(self.log)

        self.addDockWidget(Qt.BottomDockWidgetArea, log)