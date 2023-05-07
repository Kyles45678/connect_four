from board import Board
from piece import Piece

b = Board(7, 6)

b.place_piece(3, Piece(0, 0, "R"))
b.place_piece(3, Piece(0, 0, "Y"))
b.place_piece(3, Piece(0, 0, "R"))
b.place_piece(3, Piece(0, 0, "Y"))
b.place_piece(2, Piece(0, 0, "R"))
b.place_piece(1, Piece(0, 0, "Y"))
b.place_piece(4, Piece(0, 0, "R"))
b.place_piece(0, Piece(0, 0, "Y"))

# print(b)
memento = b.to_string()
# b.print_board()
# print("-------------------")
# print(memento)
# print("-------------------")
w = b.copy()
w.is_board_full()
w.print_board()
# new_b = Board()
# new_b.parse_string(memento)
# new_b.place_piece(0, Piece(0, 0, "Y"))
# print(new_b)
# new_b.print_board()
# b.print_board()

