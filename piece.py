
class Piece:
    def __init__(self, row, col, color):
        self.color = color
        self.row = row or 0
        self.col = col or 0

    def set_pos(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.color} at ({self.row}, {self.col})"

    def __repr__(self):
        return f"{self.color} at ({self.row}, {self.col})"
