from agent import Agent
from board import Board
from random_pattern import RandomPattern

COLUMNS = 7
ROWS = 6

def board_has_winner(board):


def board_can_be_played(board):
    return board.is_board_full()


def run_game(board, agent1, agent2):

    print("---------------- STARTING GAME ----------------")
    board.print_board()

    current_player = agent1
    while not board_has_winner(board) and board_can_be_played(board):
        print(str(current_player) + "'s turn!")
        current_player.play_move()
        board.print_board()
        print("-------- turn over --------")
        if current_player == agent1:
            current_player = agent2
        else:
            current_player = agent1

    if board_has_winner(board):
        print("We have a winner!")
    elif not board_can_be_played(board):
        print("Stalemate! WAAHHHH!!!!")

def main():
    board = Board(COLUMNS, ROWS)
    agent1 = Agent(board, RandomPattern(board), "Yellow")
    agent2 = Agent(board, RandomPattern(board), "Red")

    run_game(board, agent1, agent2)


main()