from agent import Agent
from board import Board
from random_pattern import RandomPattern
import time

COLUMNS = 7
ROWS = 6


def pieces_in_direction(board, color, column, row, found, column_change, row_change):
    if board.get_piece(column, row) is not None and board.get_piece(column, row).color == color:
        return pieces_in_direction(board, color, column
                                   + column_change, row + row_change, found + 1, column_change, row_change)
    return found


def board_has_winner(piece, board):
    if piece is not None:
        if (1 + (pieces_in_direction(board, piece.color, piece.col + 1, piece.row, 0, 1, 0)
                 + pieces_in_direction(board, piece.color, piece.col - 1, piece.row, 0, -1, 0))) >= 4:
            return True
        if (1 + (pieces_in_direction(board, piece.color, piece.col, piece.row + 1, 0, 0, 1)
                 + pieces_in_direction(board, piece.color, piece.col, piece.row - 1, 0, 0, -1))) >= 4:
            return True
        if (1 + (pieces_in_direction(board, piece.color, piece.col + 1, piece.row + 1, 0, 1, 1)
                 + pieces_in_direction(board, piece.color, piece.col - 1, piece.row - 1, 0, -1, -1))) >= 4:
            return True
        if (1 + (pieces_in_direction(board, piece.color, piece.col + 1, piece.row - 1, 0, 1, -1)
                 + pieces_in_direction(board, piece.color, piece.col - 1, piece.row + 1, 0, -1, 1))) >= 4:
            return True
    return False


def board_can_be_played(board):
    return not board.is_board_full()


def run_game(board, agent1, agent2):
    turns = 0
    winner = None
    start = time.perf_counter()
    print("---------------- STARTING GAME ----------------")
    board.print_board()

    current_player = agent1
    while board_can_be_played(board):
        turns += 1
        print(str(current_player) + "'s turn!")
        piece = current_player.play_move()
        board.print_board()
        if board_has_winner(piece, board):
            print("We have a winner! Its " + str(current_player) + "!")
            winner = str(current_player)
            break
        elif not board_can_be_played(board):
            print("Stalemate! WAAHHHH!!!!")
            winner = "Stalemate"
            break

        print("-------- turn over --------")
        if current_player == agent1:
            current_player = agent2
        else:
            current_player = agent1
    game_time = time.perf_counter() - start
    return [game_time, turns, winner]


def main():
    stats = [0, 0, [0, 0, 0]]
    for i in range(100):
        board = Board(COLUMNS, ROWS)
        agent1 = Agent(board, RandomPattern(board), "Yellow")
        agent2 = Agent(board, RandomPattern(board), "Red")

        game_stats = run_game(board, agent1, agent2)
        stats[0] += game_stats[0]
        stats[1] += game_stats[1]
        if game_stats[2] == "Yellow":
            stats[2][0] += 1
        elif game_stats[2] == "Red":
            stats[2][1] += 1
        else:
            stats[2][2] += 1
        print(stats)


main()
