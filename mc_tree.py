from collections import defaultdict

from agent import Agent
from random_pattern import RandomPattern


class MCTree:
    def __init__(self, board, paths_sampled):
        self.agent = None
        self.root = board

        self.paths_sampled = paths_sampled
        self.children = defaultdict(lambda: dict())
        self.children[self.root] = dict()

    def set_root(self, board):
        self.root = board

    def run_paths(self, agent):
        self.agent = agent
        for i in range(self.paths_sampled):
            current_state = self.root
            agent1 = Agent(current_state, RandomPattern(current_state), "Yellow")
            agent2 = Agent(current_state, RandomPattern(current_state), "Red")
            current_player = agent1
            leave = False
            while not current_state.is_board_full():
                next_state = current_state.copy()
                agent1.set_board(next_state)
                agent2.set_board(next_state)
                piece = current_player.play_move()
                next_state.last_played_piece = piece
                if piece is None:
                    leave = True
                    # break
                if next_state.board_has_winner(piece):
                    next_state.is_end_state = True
                    next_state.winner = current_player.name
                    # print("W")
                    leave = True
                    # break
                elif next_state.is_board_full():
                    next_state.is_end_state = True
                    next_state.winner = "Stalemate"
                    leave = True
                    # break
                if current_player == agent1:
                    current_player = agent2
                else:
                    current_player = agent1
                self.children[current_state][piece] = next_state
                current_state = next_state
                if leave is True:
                    break

    def determine_outcomes(self, root):
        root.outcomes[:] = 0
        if root.is_end_state:
            if root.winner == self.agent.name:
                root.outcomes[0] = 1
            elif root.winner == "Stalemate":
                root.outcomes[1] = 1
            else:
                root.outcomes[2] = 1
        else:
            for piece, child in self.children[root].items():
                self.determine_outcomes(child)
                root.outcomes += child.outcomes

        root.win_ratio = root.outcomes[0] / sum(root.outcomes)
        # print(root.outcomes)

    def find_policy(self):
        policy_map = dict()
        stack = [self.root]
        while len(stack) != 0:
            current = stack.pop()

            if current.is_end_state:
                continue

            best_piece = None
            best_score = 0.0
            for piece, child_state in self.children[current].items():
                stack.append(child_state)
                if child_state.win_ratio >= best_score:
                    best_score = child_state.win_ratio
                    best_piece = piece

            policy_map[current] = best_piece

        return policy_map
