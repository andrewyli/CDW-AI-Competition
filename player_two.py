from game import Game
from board import Board
import random


class Player_Two:
    def __init__(self, p):
        self.score = p  # number of boxes you have filled in

    def move(self, game):
        # Your task: fill this in!
        # should return a box duple index and which of its edges (0, 1, 2 or 3 = up right down left) to update
        # example (random) algorithm shown.
        cur_board = game.boards[len(game.boards) - 1]
        poss_moves = []
        for i in range(len(cur_board.grid)):
            for j in range(len(cur_board.grid)):
                if cur_board.grid[i][j].up == 0:
                    poss_moves.append([i, j, 0])
                if cur_board.grid[i][j].right == 0:
                    poss_moves.append([i, j, 1])
                if cur_board.grid[i][j].down == 0:
                    poss_moves.append([i, j, 2])
                if cur_board.grid[i][j].left == 0:
                    poss_moves.append([i, j, 3])
        if len(poss_moves) == 0:
            return [-1, -1, -1]
        rand_num = random.randint(0, len(poss_moves) - 1)
        return poss_moves[rand_num]
