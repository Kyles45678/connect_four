class Node:
    def __init__(self, board, piece, player_color):
        self.board = board
        # self.children = []
        self.piece = piece
        self.player_color = player_color
        self.win_fraction = 0.0

    def is_end_state(self):
        return self.board.board_has_winner(self.piece)

    def is_winner(self):
        if self.is_end_state() is True:
            return self.player_color == self.piece.color
        else:
            return False

    def get_board(self):
        return self.board

    def get_piece(self):
        return self.piece
