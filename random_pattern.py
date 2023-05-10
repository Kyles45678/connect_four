import random


class RandomPattern:

    def act(self, board_state):
        available_moves = board_state.enumerate_moves()
        chosen_move = random.choice(available_moves)
        board_state.play_move(chosen_move)

