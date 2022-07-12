from node_graphics_scene import QDMGraphicsScene


class Scene:
    def __init__(self):
        self.gr_scene = None
        self.nodes = []
        self.edges = []
        self.scene_width, self.scene_height = 64000, 64000
        self.init_ui()

    def init_ui(self):
        # create graphics scene
        self.gr_scene = QDMGraphicsScene(self)
        self.gr_scene.set_gr_scene(self.scene_width, self.scene_height)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_node(self, node):
        self.nodes.remove(node)

    def remove_edge(self, edge):
        self.edges.remove(edge)
