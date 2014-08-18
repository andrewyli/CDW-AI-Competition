class Board:
    def __init__(self, g):
        self.grid = g  # 2 dimensional array of side length 2 * GRID_SIZE + 1, contains Box(es)

    def fill_edge(self, i, j, dir, p):
        # takes a direction and a location in the grid, if edge not filled in then fill it in.
        # p is 1 or 2 depending on which player you are.
        b = self.grid[i][j]
        
        if dir == 0:
            assert b.up == 0, "Edge already filled - error"
            self.grid[i][j].up = p
            if j > 1:
                self.grid[i][j - 1].down = p
        elif dir == 1:
            edge = b.right
            assert edge == 0, "Edge already filled - error"
            self.grid[i][j].right = p
            if i < len(self.grid) - 1:
                self.grid[i + 1][j].left = p
        elif dir == 2:
            edge = b.down
            assert edge == 0, "Edge already filled - error"
            self.grid[i][j].down = p
            if j < len(self.grid) - 1:
                self.grid[i][j + 1].up = p
        else:
            assert dir == 3, "Direction not one of 0, 1, 2, or 3"
            edge = b.left
            assert edge == 0, "Edge already filled - error"
            self.grid[i][j].left = p
            if i > 1:
                self.grid[i - 1][j].right = p
