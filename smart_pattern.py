from mc_tree import MCTree
from node import Node
from piece import Piece


# from piece import Piece

#
class SmartPattern:

    def __init__(self, board, paths_sampled):
        self.paths_sampled = paths_sampled
        self.board = board.copy()
        self.tree = MCTree(self.board, paths_sampled)

    def act(self, agent):
        self.tree.set_root(self.board)
        self.tree.run_paths(agent)
        self.tree.determine_outcomes(self.tree.root)
        policy = self.tree.find_policy()
        piece = policy[self.board]
        agent.board.place_piece(piece.col, piece)
