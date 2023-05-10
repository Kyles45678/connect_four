from collections import defaultdict
import random
from board import BoardState


class MCTree:
    def __init__(self):
        self.root = BoardState()

        self.children = defaultdict(lambda: dict())
        self.children[self.root] = dict()

    def reroot_tree(self, board_state):
        self.root = board_state.copy()

    def sample_paths(self, n_paths):
        for i in range(n_paths):
            current = self.root
            while True:
                available_moves = current.enumerate_moves()
                if len(available_moves) == 0:
                    break
                chosen_move = random.choice(available_moves)
                next_state = current.copy()
                next_state.play_move(chosen_move)
                self.children[current][chosen_move] = next_state
                current = next_state

    def propagate_outcomes(self):
        return self._propagate_outcomes(self.root)

    def _propagate_outcomes(self, root):
        root.outcomes[:] = 0

        if root.is_end_state:
            # _, winner = root.determine_winner()
            winner = root.winner
            root.outcomes[winner] = 1
        else:
            for move, child in self.children[root].items():
                self._propagate_outcomes(child)
                root.outcomes += child.outcomes

        player = root.determine_previous_player()
        root.win_frac = root.outcomes[player] / sum(root.outcomes)

    def find_policy(self):
        policy_map = dict()

        stack = [self.root]
        while len(stack) != 0:
            current = stack.pop()

            if current.is_end_state:
                continue

            best_move = None
            best_score = 0.0
            for move, child_state in self.children[current].items():
                stack.append(child_state)
                if child_state.win_frac >= best_score:
                    best_score = child_state.win_frac
                    best_move = move

            policy_map[current] = best_move

        return policy_map
