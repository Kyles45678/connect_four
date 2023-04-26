class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces = [[None] * height] * width

    def place_piece(self, column, piece):
        if self.is_column_full(column):
            return -1, -1
        for i in range(0, self.height):
            if self.spaces[column][i] is not None:
                self.spaces[column][i - 1] = piece
                return i - 1, column
        self.spaces[column][self.height - 1] = piece
        return self.height-1, column

    def is_column_full(self, column):
        if self.spaces[column][0] is None:
            return False
        return True

    def get_piece(self, column, row):
        if column >= self.width or column < 0 or row >= self.height or row < 0:
            return None
        return self.spaces[column][row]

    def print_board(self):
        # board_string = ""
        for i in range(0, self.width):
            board_string = ""
            for x in range(0, self.height):
                if self.spaces[i][x] is not None:
                    board_string += str(self.spaces[i][x])
                else:
                    board_string += "*"
            # board_string += "\n"
            print(board_string)

    def clear_board(self):
        self.spaces = [[None] * self.width] * self.height

    def is_board_full(self):
        for i in range(0, self.width):
            if not self.is_column_full(i):
                return False
        return True
