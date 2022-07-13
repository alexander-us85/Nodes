from node_graphics_socket import QDMGraphicsSocket


LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket:
    def __init__(self, node, index=0, position=LEFT_TOP):
        self.node = node
        self.index = index
        self.position = position
        self.gr_socket = QDMGraphicsSocket(self.node.gr_node)
        self.gr_socket.setPos(*self.node.get_socket_position(index, position))
