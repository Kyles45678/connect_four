
class Agent:

    def __init__(self, board, init_pattern, name):
        self.board = board
        self.pattern = init_pattern
        self.name = name

    def set_pattern(self, p):
        self.pattern = p

    def set_board(self, b):
        self.board = b

    def play_move(self):
        return self.pattern.act(self)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"