
class Piece:
    def __init__(self, col, row, color):
        self.color = color
        self.col = col or 0
        self.row = row or 0

    def set_pos(self, col, row):
        self.row = row
        self.col = col

    def __str__(self):
        # return f"{self.color} at ({self.col}, {self.row})"
        return self.color[:1]

    def __repr__(self):
        return f"{self.color} at ({self.col}, {self.row})"
