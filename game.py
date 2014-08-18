from board import Board


class Game:
    def __init__(self, b):
        self.boards = b  # a list of boards

    def finished(self):  # if all cells are filled
        cur_board = self.boards[len(self.boards) - 1]
        for i in range(len(cur_board.grid)):
            for j in range(len(cur_board.grid)):
                if not cur_board.grid[i][j].filled:
                    return False
        return True
