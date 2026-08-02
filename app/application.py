from PyQt6.QtWidgets import QApplication

import sys


class AngryBirdApplication:

    def __init__(self):
        self.app = QApplication(sys.argv)

    def run(self, window):
        window.show()
        sys.exit(self.app.exec())