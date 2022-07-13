from graphics_node import QDMGraphicsNode
from node_content_widget import QDMNodeContentWidget
from node_socket import *


class Node:
    def __init__(self, scene, title="Untitled Node", inputs=None, outputs=None):
        if outputs is None:
            outputs = []
        if inputs is None:
            inputs = []

        self._socket_spacing = 22

        self.scene = scene
        self.title = title

        self.content = QDMNodeContentWidget()
        self.gr_node = QDMGraphicsNode(self)

        self.scene.add_node(self)
        self.scene.gr_scene.addItem(self.gr_node)

        self.inputs = []
        self.outputs = []

        for index, item in enumerate(inputs):
            socket = Socket(node=self, index=index, position=LEFT_TOP)
            self.inputs.append(socket)

        for index, item in enumerate(outputs):
            socket = Socket(node=self, index=index, position=RIGHT_TOP)
            self.outputs.append(socket)

    def get_socket_position(self, index, position):
        x = 0 if position in (LEFT_TOP, LEFT_BOTTOM) else self.gr_node.width
        if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
            y = self.gr_node.height - self.gr_node.edge_size - index * self._socket_spacing
        else:
            y = self._get_top_offset() + index * self._socket_spacing
        return x, y

    def _get_top_offset(self):
        return self.gr_node.title_height + 15
