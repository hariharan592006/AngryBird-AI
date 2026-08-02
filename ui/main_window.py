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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.build_ui()

    def build_ui(self):

        central_widget = QWidget()

        main_layout = QVBoxLayout()

        # Top Bar
        self.top_bar = TopBar()
        main_layout.addWidget(self.top_bar)

        self.chat_area = ChatArea()

        main_layout.addWidget(self.chat_area)

        self.message_input = MessageInput()

        main_layout.addWidget(self.message_input)

        # Remove extra spacing
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)