import random
from piece import Piece


class RandomPattern:

    def __init__(self, board):
        self.board = board

    def act(self, agent):
        playable_columns = []
        for c in range(self.board.width):
            if not self.board.is_column_full(c):
                playable_columns.append(c)

        if len(playable_columns) > 0:
            chosen_col = random.choice(playable_columns)
            piece = Piece(0, 0, agent.name)
            (placed_row, placed_col) = self.board.place_piece(chosen_col, piece)
            if placed_row == -1:
                return None
            piece.set_pos(placed_row, placed_col)
            return piece
        else:
            return None

