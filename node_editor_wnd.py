from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from node_scene import Scene
from node_graphics_view import QDMGraphicsView


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene = None
        self.view = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.setLayout(self.layout)

        self.scene = Scene()

        # create graphics view
        self.view = QDMGraphicsView(self.scene, self)
        self.view.setScene(self.scene.gr_scene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

        self.add_debug_content()

    def add_debug_content(self):
        green_brush = QBrush(Qt.green)
        outline_pen = QPen(Qt.black)
        outline_pen.setWidth(2)

        rect = self.scene.gr_scene.addRect(-100, -100, 80, 100, outline_pen, green_brush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        line = self.scene.gr_scene.addLine(-200, 100, 200, 300, outline_pen)
