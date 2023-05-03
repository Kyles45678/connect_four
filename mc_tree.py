class MCTree:
    def __init__(self, root_node, paths_sampled):
        self.root = root_node
        self.paths_sampled = paths_sampled

    def set_root(self, node):
        self.root = node
