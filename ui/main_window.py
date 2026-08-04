from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from shared.version import APP_NAME
from shared.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from ui.components.top_bar import TopBar
from ui.components.chat_area import ChatArea
from ui.components.message_input import MessageInput
from ui.components.status_bar import StatusBar

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.build_ui()

    def connect_signals(self):
        """
        Connect UI components together.
        """

        self.message_input.send_button.clicked.connect(
            self.send_message
        )

    def send_message(self):

        text = self.message_input.input_box.toPlainText().strip()

        if not text:
            return

        print("User:", text)

        self.status_bar.set_status("Message Sent")

        self.message_input.input_box.clear()

    def build_ui(self):

        central_widget = QWidget()

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.top_bar = TopBar()
        main_layout.addWidget(self.top_bar)

        self.chat_area = ChatArea()

        # ⭐ Give the chat area all remaining space
        main_layout.addWidget(self.chat_area, 1)

        self.message_input = MessageInput()
        main_layout.addWidget(self.message_input)

        self.status_bar = StatusBar()
        main_layout.addWidget(self.status_bar)

        self.connect_signals()

        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)