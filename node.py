from graphics_node import QDMGraphicsNode
from node_content_widget import QDMNodeContentWidget


class Node:
    def __init__(self, scene, title="Untitled Node", inputs=None, outputs=None):
        if outputs is None:
            outputs = []
        if inputs is None:
            inputs = []

        self.scene = scene
        self.title = title

        self.content = QDMNodeContentWidget()
        self.gr_node = QDMGraphicsNode(self)

        self.scene.add_node(self)
        self.scene.gr_scene.addItem(self.gr_node)

        self.inputs = []
        self.outputs = []

