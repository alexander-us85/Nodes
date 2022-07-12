from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.wdg_label = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.wdg_label = QLabel("Some title")
        self.wdg_label.setContentsMargins(4, 0, 0, 0)
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit("Foo"))
