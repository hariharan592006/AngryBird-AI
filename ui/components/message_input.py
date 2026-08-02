from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)


class MessageInput(QWidget):
    """
    Message input area.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QHBoxLayout()

        self.input_box = QTextEdit()

        self.input_box.setPlaceholderText(
            "Type a message..."
        )

        self.input_box.setFixedHeight(60)

        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(60, 60)

        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.setStyleSheet("""
            QTextEdit{
                background:#303030;
                color:white;
                border-radius:10px;
                padding:8px;
                font-size:15px;
            }

            QPushButton{
                background:#ff9800;
                color:black;
                border-radius:10px;
                font-size:18px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#ffb74d;
            }
        """)