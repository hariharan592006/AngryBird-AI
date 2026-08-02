from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt


class ChatArea(QWidget):
    """
    Displays the conversation area.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        welcome = QLabel(
            """
👋 Welcome to Angry Bird

I'm your personal AI assistant.

Right now I'm offline.

Soon I'll be able to:

• Chat with you
• Remember things
• Control your laptop
• Synchronize with your phone
• Complete your missions

Let's begin...
"""
        )

        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome.setStyleSheet("""
            color:white;
            font-size:18px;
            padding:40px;
        """)

        layout.addStretch()
        layout.addWidget(welcome)
        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
            background-color:#2b2b2b;
        """)