from agent import Agent
from board import Board
from random_pattern import RandomPattern
import time

from smart_pattern import SmartPattern

COLUMNS = 7
ROWS = 6


def board_can_be_played(board):
    return not board.is_board_full()


def run_game(board, agent1, agent2):
    turns = 0
    winner = None
    start = time.perf_counter()
    # print("---------------- STARTING GAME ----------------")
    # board.print_board()

    current_player = agent1
    while board_can_be_played(board):
        turns += 1
        print(str(current_player) + "'s turn!")
        piece = current_player.play_move()
        # board.last_played_piece = piece
        board.print_board()
        if board.board_has_winner(piece):
            # board.is_end_state = True
            # board.winner = current_player.color
            print("We have a winner! Its " + str(current_player) + "!")
            winner = str(current_player)
            break
        elif not board_can_be_played(board):
            # board.is_end_state = True
            # board.winner = "Stalemate"
            print("Stalemate! WAAHHHH!!!!")
            winner = "Stalemate"
            break

        # print("-------- turn over --------")
        if current_player == agent1:
            current_player = agent2
        else:
            current_player = agent1
    game_time = time.perf_counter() - start
    return [game_time, turns, winner]


def main():
    stats = [0, 0, [0, 0, 0]]
    for i in range(1):
        board = Board(COLUMNS, ROWS)
        agent1 = Agent(board, SmartPattern(board, 1), "Yellow")
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
