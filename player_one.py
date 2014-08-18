from game import Game
from board import Board


class Player_One:
    
    def __init__(self, p):
        self.score = p  # number of boxes you have filled in

    def move(self, game):
        # Your task: fill this in!
        # should return a box duple index and which of its edges (0, 1, 2 or 3 = up right down left) to update
        # example (dumb) algorithm shown.
        cur_board = game.boards[len(game.boards) - 1]
        for i in range(len(cur_board.grid)):
            for j in range(len(cur_board.grid)):
                if cur_board.grid[i][j].up == 0:
                    return [i, j, 0]
                elif cur_board.grid[i][j].right == 0:
                    return [i, j, 1]
                elif cur_board.grid[i][j].down == 0:
                    return [i, j, 2]
                elif cur_board.grid[i][j].left == 0:
                    return [i, j, 3]
        return [-1, -1, -1]
