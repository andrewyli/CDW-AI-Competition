from board import Board


class Game:
    def __init__(self, b):
        self.boards = b  # a list of boards

    def finished(self):  # if there exists more squares to be filled
        if self.fill_count() == len(self.boards[0].grid) ** 2:
            return True
        return False

    def fill_count(self):
        count = 0
        for i in range(len(self.boards[0].grid)):
            for j in range(len(self.boards[0].grid)):
                if self.boards[len(self.boards) - 1].grid[i][j].filled:
                    count += 1
        return count
        
