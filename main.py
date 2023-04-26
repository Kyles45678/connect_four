from agent import Agent
from board import Board
from random_pattern import RandomPattern

COLUMNS = 7
ROWS = 6


def pieces_in_direction(board, color, column, row, found, column_change, row_change):
    if board.get_piece(column, row) is not None and board.get_piece(column, row).color == color:
        return pieces_in_direction(board, color, column
                                   + column_change, row + row_change, found + 1, column_change, row_change)
    return found


def board_has_winner(piece, board):
    if piece is not None:
        found = (pieces_in_direction(board, piece.color, piece.column, piece.row, 1, 1, 0)
                 + pieces_in_direction(board, piece.color, piece.column, piece.row, 1, -1, 0))
        if found >= 4:
            return True
        found = (pieces_in_direction(board, piece.color, piece.column, piece.row, 1, 0, 1)
                 + pieces_in_direction(board, piece.color, piece.column, piece.row, 1, 0, -1))
        if found >= 4:
            return True
        found = (pieces_in_direction(board, piece.color, piece.column, piece.row, 1, 1, 1)
                 + pieces_in_direction(board, piece.color, piece.column, piece.row, 1, -1, -1))
        if found >= 4:
            return True
        found = (pieces_in_direction(board, piece.color, piece.column, piece.row, 1, 1, -1)
                 + pieces_in_direction(board, piece.color, piece.column, piece.row, 1, -1, 1))
        if found >= 4:
            return True
        pass
    return False


def board_can_be_played(board):
    return not board.is_board_full()


def run_game(board, agent1, agent2):
    print("---------------- STARTING GAME ----------------")
    board.print_board()

    current_player = agent1
    # print(board.width)
    # print(board.spaces[0][0])
    print(board_can_be_played(board))
    while board_can_be_played(board):
        print(str(current_player) + "'s turn!")
        piece = current_player.play_move()
        if board_has_winner(piece, board):
            print("We have a winner!")
            break
        elif not board_can_be_played(board):
            print("Stalemate! WAAHHHH!!!!")
            break
        board.print_board()
        print("-------- turn over --------")
        if current_player == agent1:
            current_player = agent2
        else:
            current_player = agent1

    # if board_has_winner(board):
    #     print("We have a winner!")
    # elif not board_can_be_played(board):
    #     print("Stalemate! WAAHHHH!!!!")


def main():
    board = Board(COLUMNS, ROWS)
    agent1 = Agent(board, RandomPattern(board), "Yellow")
    agent2 = Agent(board, RandomPattern(board), "Red")

    run_game(board, agent1, agent2)


main()
