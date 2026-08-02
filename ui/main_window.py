from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import Qt

from shared.version import APP_NAME, FULL_VERSION
from shared.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    STATUS_READY,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        label = QLabel(
            f"""
🐦 {APP_NAME}

Version : {FULL_VERSION}

Status : {STATUS_READY}
"""
        )

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)