import copy

from piece import Piece


class Board:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
        self.spaces = [[None for i in range(height)] for j in range(width)]
        # possible other needed vars
        # self.last_played_piece = None
        # self.is_end_state = False
        # self.win_ratio = 0.0
        # self.winner = None
        # self.outcomes = np.zeros(3, int)


    def place_piece(self, column, piece):
        if self.is_column_full(column):
            return -1, -1
        for i in range(0, self.height):
            if self.spaces[column][i] is not None:
                self.spaces[column][i - 1] = piece
                return column, i - 1
        self.spaces[column][self.height - 1] = piece
        return column, self.height - 1

    def is_column_full(self, column):
        if self.spaces[column][0] is None:
            return False
        return True

    def get_piece(self, column, row):
        if column >= self.width or column < 0 or row >= self.height or row < 0:
            return None
        return self.spaces[column][row]

    def print_board(self):
        print(self.to_string())

    def clear_board(self):
        self.spaces = [[None for i in range(self.height)] for j in range(self.width)]

    def is_board_full(self):
        for i in range(0, self.width):
            if not self.is_column_full(i):
                return False
        return True

    def to_string(self):
        board_string = ""
        for i in range(self.height):
            for x in range(self.width):
                if self.spaces[x][i] is not None:
                    board_string += str(self.spaces[x][i])
                else:
                    board_string += "*"
                board_string += " "
            board_string = board_string.strip()
            board_string += "\n"
        return board_string.strip();

    def parse_string(self, string):
        lines = string.strip().split("\n")
        self.height = len(lines)
        self.width = len(lines[0].strip().split(" "))
        self.clear_board()
        for r in range(self.height):
            line = lines[r].strip().split(" ")
            for c in range(self.width):
                char = line[c]
                if char == "*":
                    self.spaces[c][r] = None
                else:
                    p = Piece(c, r, char)
                    self.spaces[c][r] = p

    def pieces_in_direction(self, color, column, row, found, column_change, row_change):
        if self.get_piece(column, row) is not None and self.get_piece(column, row).color == color:
            return self.pieces_in_direction(color, column
                                            + column_change, row + row_change, found + 1, column_change, row_change)
        return found

    def board_has_winner(self, piece):
        if piece is not None:
            if (1 + (self.pieces_in_direction(piece.color, piece.col + 1, piece.row, 0, 1, 0)
                     + self.pieces_in_direction(piece.color, piece.col - 1, piece.row, 0, -1, 0))) >= 4:
                return True
            if (1 + (self.pieces_in_direction(piece.color, piece.col, piece.row + 1, 0, 0, 1)
                     + self.pieces_in_direction(piece.color, piece.col, piece.row - 1, 0, 0, -1))) >= 4:
                return True
            if (1 + (self.pieces_in_direction(piece.color, piece.col + 1, piece.row + 1, 0, 1, 1)
                     + self.pieces_in_direction(piece.color, piece.col - 1, piece.row - 1, 0, -1, -1))) >= 4:
                return True
            if (1 + (self.pieces_in_direction(piece.color, piece.col + 1, piece.row - 1, 0, 1, -1)
                     + self.pieces_in_direction(piece.color, piece.col - 1, piece.row + 1, 0, -1, 1))) >= 4:
                return True
        return False

    def find_possible_moves(self):
        playable_columns = []
        for c in range(self.width):
            if not self.is_column_full(c):
                playable_columns.append(c)
        return playable_columns

    def copy(self):
        b = Board()
        b.spaces = copy.deepcopy(self.spaces)
        b.width = self.width
        b.height = self.height
        return b
