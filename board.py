class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces = [[None for i in range(height)] for j in range(width)]

    def place_piece(self, column, piece):
        if self.is_column_full(column):
            return -1, -1
        for i in range(0, self.height):
            if self.spaces[column][i] is not None:
                self.spaces[column][i - 1] = piece
                return column, i - 1
        self.spaces[column][self.height - 1] = piece
        return column, self.height-1

    def is_column_full(self, column):
        if self.spaces[column][0] is None:
            return False
        return True

    def get_piece(self, column, row):
        if column >= self.width or column < 0 or row >= self.height or row < 0:
            return None
        return self.spaces[column][row]

    def print_board(self):
        for i in range(0, self.height):
            board_string = ""
            for x in range(0, self.width):
                if self.spaces[x][i] is not None:
                    board_string += str(self.spaces[x][i])
                else:
                    board_string += "*"
            print(board_string)

    def clear_board(self):
        self.spaces = [[None] * self.width] * self.height

    def is_board_full(self):
        for i in range(0, self.width):
            if not self.is_column_full(i):
                return False
        return True
