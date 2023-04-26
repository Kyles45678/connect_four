class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces = [[None] * width] * height
        pass

    def place_piece(self, column, piece):
        if self.is_column_full(column):
            return False
        for i in range(0, len(self.spaces[column])):
            if self.spaces[column][i] is not None:
                self.spaces[column][i - 1] = piece
                return True

    def is_column_full(self, column):
        if self.spaces[column][0] is None:
            return False
        return True

    def get_piece(self, column, row):
        return self.spaces[column][row]

    def print_board(self):
        board_string = ""
        for i in range(0, len(self.spaces)):
            for x in range(0, len(self.spaces[i])):
                if self.spaces[i][x] is not None:
                    board_string += str(self.spaces[i][x])
                else:
                    board_string += "*"
            board_string += "\n"

    def clear_board(self):
        self.spaces = [[None] * self.width] * self.height
