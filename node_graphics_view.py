from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.grScene = scene.gr_scene
        self.init_ui()
        self.setScene(self.grScene)

        self.zoom_in_factor = 1.25
        self.zoom_clamp = True
        self.zoom = 10
        self.zoom_step = 1
        self.zoom_range = [0, 10]

    def init_ui(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, mouse_event):
        if mouse_event.button() == Qt.MiddleButton:
            self.middle_mouse_button_press(mouse_event)
        elif mouse_event.button() == Qt.LeftButton:
            self.left_mouse_button_press(mouse_event)
        elif mouse_event.button() == Qt.RightButton:
            self.right_mouse_button_press(mouse_event)
        else:
            super().mousePressEvent(mouse_event)

    def mouseReleaseEvent(self, mouse_event):
        if mouse_event.button() == Qt.MiddleButton:
            self.middle_mouse_button_release(mouse_event)
        elif mouse_event.button() == Qt.LeftButton:
            self.left_mouse_button_release(mouse_event)
        elif mouse_event.button() == Qt.RightButton:
            self.right_mouse_button_release(mouse_event)
        else:
            super().mouseReleaseEvent(mouse_event)

    def middle_mouse_button_press(self, mouse_event):
        release_event = QMouseEvent(QEvent.MouseButtonRelease, mouse_event.localPos(),
                                    mouse_event.screenPos(), Qt.LeftButton, Qt.NoButton,
                                    mouse_event.modifiers())
        super().mouseReleaseEvent(release_event)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fake_event = QMouseEvent(mouse_event.type(), mouse_event.localPos(), mouse_event.screenPos(),
                                 Qt.LeftButton, mouse_event.buttons() | Qt.LeftButton, mouse_event.modifiers())
        super().mousePressEvent(fake_event)

    def middle_mouse_button_release(self, mouse_event):
        fake_event = QMouseEvent(mouse_event.type(), mouse_event.localPos(), mouse_event.screenPos(),
                                 Qt.LeftButton, mouse_event.buttons() & -Qt.LeftButton, mouse_event.modifiers())
        super().mouseReleaseEvent(fake_event)
        self.setDragMode(QGraphicsView.NoDrag)

    def left_mouse_button_press(self, mouse_event):
        return super().mousePressEvent(mouse_event)

    def right_mouse_button_press(self, mouse_event):
        return super().mousePressEvent(mouse_event)

    def left_mouse_button_release(self, mouse_event):
        return super().mouseReleaseEvent(mouse_event)

    def right_mouse_button_release(self, mouse_event):
        return super().mouseReleaseEvent(mouse_event)

    def wheelEvent(self, wheel_event):
        # calculate zoom factor
        zoom_out_factor = 1 / self.zoom_in_factor

        # calculate zoom
        if wheel_event.angleDelta().y() > 0:
            zoom_factor = self.zoom_in_factor
            self.zoom += self.zoom_step
        else:
            zoom_factor = zoom_out_factor
            self.zoom -= self.zoom_step

        clamped = False
        if self.zoom < self.zoom_range[0]: self.zoom, clamped = self.zoom_range[0], True
        if self.zoom > self.zoom_range[1]: self.zoom, clamped = self.zoom_range[1], True

        if not clamped or self.zoom_clamp is False:
            self.scale(zoom_factor, zoom_factor)
