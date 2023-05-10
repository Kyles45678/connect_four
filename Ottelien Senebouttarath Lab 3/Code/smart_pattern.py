from board import BoardState


class SmartPattern:
    def __init__(self, tree, paths_sampled):
        self.tree = tree
        self.paths_sampled = paths_sampled

    def act(self, board_state: BoardState):
        self.tree.reroot_tree(board_state)
        self.tree.sample_paths(self.paths_sampled)
        self.tree.propagate_outcomes()
        policy = self.tree.find_policy()
        move = policy[board_state]
        board_state.play_move(move)
