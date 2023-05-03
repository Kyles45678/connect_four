from agent import Agent
from main import run_game
from mc_tree import MCTree
from random_pattern import RandomPattern


# from piece import Piece

#
class SmartPattern:

    def __init__(self, board, paths_sampled):
        self.paths_sampled = paths_sampled
        self.board = board
        self.tree = MCTree(board, paths_sampled)
        # self.sub_agent = Agent(board, sub_pattern, name)

    def act(self, agent):
        return None
        # playable_columns = []
        # for c in range(self.board.width):
        #     if not self.board.is_column_full(c):
        #         playable_columns.append(c)
        #
        # if len(playable_columns) > 0:
        #     chosen_col = random.choice(playable_columns)
        #     piece = Piece(0, 0, agent.name)
        #     (placed_col, placed_row) = self.board.place_piece(chosen_col, piece)
        #     if placed_row == -1:
        #         return None
        #     piece.set_pos(placed_col, placed_row)
        #     return piece
        # else:
        #     return None

    def run_paths(self):
        for i in range(self.paths_sampled):
            data = run_game(self.tree.root.get_board(),
                            Agent(self.tree.root.get_board(),
                                  RandomPattern(self.tree.root.get_board()), "Yellow"),
                            Agent(self.tree.root.get_board(),
                                  RandomPattern(self.tree.root.get_board()), "Red"))
            # return 1
        return None
