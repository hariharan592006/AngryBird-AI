from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from shared.version import APP_NAME


class TopBar(QWidget):
    """
    Top navigation bar of Angry Bird.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

        self.setFixedHeight(60)

    def build_ui(self):

        layout = QHBoxLayout()

        # App Name
        title = QLabel(f"🐦 {APP_NAME}")
        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:white;
        """)

        # Status
        status = QLabel("Offline")
        status.setStyleSheet("""
            color:orange;
            font-size:13px;
        """)

        # Settings Button
        settings_button = QPushButton("⚙")

        settings_button.setFixedWidth(40)

        layout.addWidget(title)

        layout.addStretch()

        layout.addWidget(status)

        layout.addSpacing(15)

        layout.addWidget(settings_button)

        self.setLayout(layout)

        self.setStyleSheet("""
            background-color:#202123;
            padding:10px;
        """)