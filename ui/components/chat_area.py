from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from ui.components.message_bubble import MessageBubble


class ChatArea(QWidget):
    """
    Displays the conversation area.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        layout.addStretch()

        welcome = MessageBubble(
    "Angry Bird",
    "👋 Welcome Hari!\n\nI'm Angry Bird.\n\nI'm currently offline, but soon I'll become your personal AI companion."
        )

        layout.addWidget(welcome)

        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
    background-color:#2b2b2b;
""")