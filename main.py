import time
from agent import Agent
from board import BoardState
from mctree import MCTree
from random_pattern import RandomPattern
from smart_pattern import SmartPattern

PLAYER1 = 1
PLAYER2 = 2


def play_game(agent1, agent2):
    board_state = BoardState()
    current_agent = agent1
    other_agent = agent2
    turns = 0
    while not board_state.is_end_state:
        turns += 1
        current_agent.play_move(board_state)
        tmp = current_agent
        current_agent = other_agent
        other_agent = tmp

    return [turns, board_state.winner]


def analysis(num_of_games, agent1_pattern, agent2_pattern):
    stats = [0, 0, [0, 0, 0]]
    start = time.perf_counter()
    for i in range(num_of_games):
        game_stats = play_game(Agent(agent1_pattern), Agent(agent2_pattern))
        stats[1] += game_stats[0]
        if game_stats[1] == PLAYER1:
            stats[2][0] += 1
        elif game_stats[1] == PLAYER2:
            stats[2][1] += 1
        else:
            stats[2][2] += 1
    stats[0] = time.perf_counter() - start
    print(stats)


analysis(50, RandomPattern(), SmartPattern(MCTree(), 10))
# analysis(50, SmartPattern(MCTree(), 10), RandomPattern())
