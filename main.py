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
    # print(board_state)
    while not board_state.is_end_state:
        # print()
        turns += 1
        current_agent.play_move(board_state)
        # print(board_state)
        tmp = current_agent
        current_agent = other_agent
        other_agent = tmp
    # print("The winner is: " + str(board_state.winner))
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


play_game(Agent(RandomPattern()), Agent(SmartPattern(MCTree(), 10)))
# analysis(100, RandomPattern(), RandomPattern())
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 1))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 2))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 3))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 4))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 5))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 6))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 7))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 8))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 9))
# analysis(100, RandomPattern(), SmartPattern(MCTree(), 10))
print("---------end of random first-----------")
# analysis(100, SmartPattern(MCTree(), 1), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 2), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 3), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 4), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 5), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 6), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 7), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 8), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 9), RandomPattern())
# analysis(100, SmartPattern(MCTree(), 10), RandomPattern())
