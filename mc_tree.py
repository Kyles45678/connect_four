from collections import defaultdict

from agent import Agent
from board import Board
from node import Node
from piece import Piece
from random_pattern import RandomPattern
import random


class MCTree:
    def __init__(self, board, paths_sampled):
        # self.agent = agent
        self.agent = None
        self.root = board.copy()

        self.paths_sampled = paths_sampled
        self.children = defaultdict(lambda: dict())
        self.children[self.root] = dict()

    def set_root(self, board):
        self.root = board.copy()

    def run_paths(self, agent):
        # self.agent = agent
        for i in range(self.paths_sampled):
            current_state = self.root.copy()
            agent1 = Agent(current_state, RandomPattern(current_state), "Yellow")
            agent2 = Agent(current_state, RandomPattern(current_state), "Red")
            current_player = agent1
            # current_state.print_board()
            while not current_state.is_board_full():
                # current_state.print_board()
                # print("--------------------")
                piece = current_player.play_move()
                # current_state.last_played_piece = piece

                next_state = current_state.copy()
                # next_state.print_board()
                # print(piece)
                # print("--------------------")
                if piece is None:
                    break
                if current_state.board_has_winner(piece):
                    # current_state.is_end_state = True
                    # current_state.winner = current_player.color
                    # print("W")
                    break
                elif current_state.is_board_full():
                    # current_state.is_end_state = True
                    # current_state.winner = "Stalemate"
                    # print("S")
                    break
                if current_player == agent1:
                    current_player = agent2
                else:
                    current_player = agent1
                self.children[current_state][piece] = next_state
                agent1.set_board(next_state)
                agent2.set_board(next_state)
                current_state = next_state

    # def determine_outcomes(self, root):
    #     # clear outcomes
    #     root.outcomes[:] = 0
    #
        # if root.is_end_state:
        #     if root.winner == agent.color:
        #         root.outcomes[0] = 1
        #     elif root.winner == "Stalemate":
        #         root.outcomes[1] = 1
        #     else:
        #         root.outcomes[2] = 1
        # else:
    #         for piece, child in self.children[root].items():
    #             self._propagate_outcomes(child)
    #             root.outcomes += child.outcomes
    #
    #     root.win_frac = root.outcomes[0] / sum(root.outcomes)



    # def find_policy(self):
    #     policy_map = dict()
    #
    #     # modified DFS
    #     stack = [self.root]
    #     while len(stack) != 0:
    #         current = stack.pop()
    #
    #         if current.is_end_state():
    #             continue
    #
    #         best_piece = None
    #         best_score = 0.0
    #         for piece, child_state in self.children[current].items():
    #             stack.append(child_state)
    #             # some states will be no-win scenarios
    #             # so the win_frac will be 0
    #             if child_state.win_frac >= best_score:
    #                 best_score = child_state.win_frac
    #                 best_piece = move
    #
    #         policy_map[current] = best_piece
    #
    #     return policy_map


