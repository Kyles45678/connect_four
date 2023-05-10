import numpy as np

from move import Move

PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0


class BoardState:
    def __init__(self, board=None):
        if board is None:
            self.board = np.zeros((6, 7), int)
        else:
            self.board = board

        self.n_rows = 6
        self.n_columns = 7
        self.outcomes = np.zeros(3, int)
        self.win_frac = 0.0
        self.is_end_state = False
        self.winner = None

    def in_board(self, row, column):
        if 0 <= column < self.n_columns and 0 <= row < self.n_rows:
            return True
        return False

    def pieces_in_direction(self, move, column, row, found, column_change, row_change):
        if self.in_board(row, column) and self.board[row, column] == move.player:
            return self.pieces_in_direction(move, column
                                            + column_change, row + row_change, found + 1, column_change, row_change)
        return found

    def board_has_winner(self, move):
        if (1 + (self.pieces_in_direction(move, move.column + 1, move.row, 0, 1, 0)
                 + self.pieces_in_direction(move, move.column - 1, move.row, 0, -1, 0))) >= 4:
            return True
        if (1 + (self.pieces_in_direction(move, move.column, move.row + 1, 0, 0, 1)
                 + self.pieces_in_direction(move, move.column, move.row - 1, 0, 0, -1))) >= 4:
            return True
        if (1 + (self.pieces_in_direction(move, move.column + 1, move.row + 1, 0, 1, 1)
                 + self.pieces_in_direction(move, move.column - 1, move.row - 1, 0, -1, -1))) >= 4:
            return True
        if (1 + (self.pieces_in_direction(move, move.column + 1, move.row - 1, 0, 1, -1)
                 + self.pieces_in_direction(move, move.column - 1, move.row + 1, 0, -1, 1))) >= 4:
            return True
        return False

    def is_initial_state(self):
        return (self.board == EMPTY).all()

    def __hash__(self):
        return hash(tuple(self.board.flatten()))

    def __eq__(self, other):
        return (self.board == other.board).all()

    def __repr__(self):
        return str(self.board)

    def determine_next_player(self):
        n_player1_pieces = np.count_nonzero(self.board.flatten() == PLAYER_1)
        n_player2_pieces = np.count_nonzero(self.board.flatten() == PLAYER_2)

        if n_player1_pieces == n_player2_pieces:
            next_player = PLAYER_1
        else:
            next_player = PLAYER_2

        return next_player

    def determine_previous_player(self):
        n_player1_pieces = np.count_nonzero(self.board.flatten() == PLAYER_1)
        n_player2_pieces = np.count_nonzero(self.board.flatten() == PLAYER_2)

        if n_player1_pieces == 0 and n_player2_pieces == 0:
            player = EMPTY
        elif n_player1_pieces == n_player2_pieces:
            player = PLAYER_2
        else:
            player = PLAYER_1

        return player

    def enumerate_moves(self):
        if self.is_end_state:
            return []

        next_player = self.determine_next_player()

        moves = []
        for c in range(self.n_columns):
            if not self.is_column_full(c):
                r = self.get_row(c)
                move = Move(next_player, r, c)
                moves.append(move)
        return moves

    def is_column_full(self, column):
        if self.board[0, column] == EMPTY:
            return False
        return True

    def get_row(self, column):
        for i in range(0, self.n_rows):
            if self.board[i, column] != EMPTY:
                return i - 1
        return self.n_rows-1

    def is_board_full(self):
        for i in range(0, self.n_columns):
            if not self.is_column_full(i):
                return False
        return True

    def play_move(self, move: Move):
        if self.board[move.row, move.column] != EMPTY:
            print(self.board, move)
            print(self.board[move.row, move.column], EMPTY)
            raise Exception("Cannot place piece at (r, c)".format(move.row, move.column))
        else:
            self.board[move.row, move.column] = move.player
            is_winner = self.board_has_winner(move)
            if is_winner:
                self.is_end_state = True
                self.winner = move.player
            elif self.is_board_full():
                self.is_end_state = True
                self.winner = 0

    def copy(self):
        b = BoardState(self.board.copy())
        b.winner = self.winner
        b.is_end_state = self.is_end_state
        return b
