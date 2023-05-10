from board import BoardState


class Agent:

    def __init__(self, init_pattern):
        self.pattern = init_pattern

    def play_move(self, board_state: BoardState):
        return self.pattern.act(board_state)
