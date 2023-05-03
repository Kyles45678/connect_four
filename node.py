class Node:
    def __init__(self, board):
        self.board = board
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def get_child(self, index):
        return self.children[index]

    def get_board(self):
        return self.board
