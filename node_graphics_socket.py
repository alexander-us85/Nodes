from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 6.0
        self._color_background = QColor("#ffff7700")
        self._color_outline = QColor("#ff00000000")

        self._pen = QPen(self._color_outline)
        self._brush = QBrush(self._color_background)

