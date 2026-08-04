from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout


class StatusBar(QWidget):
    """
    Bottom status bar.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QHBoxLayout()

        self.status_label = QLabel("Status : Ready")

        self.status_label.setStyleSheet("""
            color:#cccccc;
            font-size:13px;
            padding-left:8px;
        """)

        layout.addWidget(self.status_label)

        layout.addStretch()

        self.setLayout(layout)

        self.setFixedHeight(35)

        self.setStyleSheet("""
            background:#202123;
        """)

    def set_status(self, text: str):
        self.status_label.setText(f"Status : {text}")