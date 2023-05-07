import random
from piece import Piece


class RandomPattern:

    def __init__(self, board):
        self.board = board

    def act(self, agent):
        playable_columns = self.board.find_possible_moves()

        if len(playable_columns) > 0:
            chosen_col = random.choice(playable_columns)
            piece = Piece(0, 0, agent.name)
            (placed_col, placed_row) = self.board.place_piece(chosen_col, piece)
            if placed_row == -1:
                return None
            piece.set_pos(placed_col, placed_row)
            return piece
        else:
            return None

