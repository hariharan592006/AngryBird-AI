from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

from PyQt6.QtCore import Qt


class MessageBubble(QFrame):
    """
    Reusable chat message bubble.
    """

    def __init__(self, sender: str, message: str):
        super().__init__()

        self.sender = sender
        self.message = message

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        sender_label = QLabel(self.sender)
        sender_label.setStyleSheet("""
            color:#ff9800;
            font-weight:bold;
            font-size:14px;
        """)

        message_label = QLabel(self.message)
        message_label.setWordWrap(True)

        message_label.setStyleSheet("""
            color:white;
            font-size:15px;
        """)

        layout.addWidget(sender_label)
        layout.addWidget(message_label)

        self.setLayout(layout)

        self.setStyleSheet("""
            QFrame{
                background:#353535;
                border-radius:12px;
                padding:12px;
            }
        """)