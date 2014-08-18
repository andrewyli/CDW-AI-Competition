from game import Game
from board import Board

import random


class Player_One:
    
    def __init__(self, p):
        self.score = p  # number of boxes you have filled in

    def move(self, game):
        # Your task: fill this in!
        # should return a box duple index and which of its edges (0, 1, 2 or 3 = up right down left) to update
        # example (dumb) algorithm shown.
        
        #print "Score: " + str(self.score)
        cur_board = game.boards[len(game.boards) - 1]
        '''
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
        '''
        size = len(cur_board.grid)
    
        gridboxes = []
        temp = []
        for i in range(size):
            temp.append(0)
        for i in range(size):
            gridboxes.append(temp)
        
        
        for i in range(size):
            for j in range(size):
                gridboxes[i][j] = (cur_board.grid[i][j].down + cur_board.grid[i][j].right + cur_board.grid[i][j].up + cur_board.grid[i][j].left)
                
        
        for i in range(size):
            for j in range(size):
                if(gridboxes[i][j] == 3):
                    if(cur_board.grid[i][j].down == 0):
                        return [i, j, 2]
                    if(cur_board.grid[i][j].right == 0):
                        return [i, j, 1]
                    if(cur_board.grid[i][j].up == 0):
                        return [i, j, 0]
                    if(cur_board.grid[i][j].left == 0):
                        return [i, j, 3]
        
        moves = []
        
        #i is x, j is y
        
        for i in range(size):
            for j in range(size):
                if(gridboxes[i][j] <= 1):
                    if(i > 0):
                        if(gridboxes[i - 1][j] <= 1):
                            if(cur_board.grid[i][j].left== 0):
                                moves.append([i, j, 3])
                    if(i < size - 1):
                        if(gridboxes[i+1][j] <= 1):
                            if(cur_board.grid[i][j].right == 0):
                                moves.append([i, j, 1])
                    if(j > 0):
                        if(gridboxes[i][j - 1] <= 1):
                            if(cur_board.grid[i][j].up == 0):
                                moves.append([i, j, 0])
                    if(j < size - 1):
                        if(gridboxes[i][j + 1] <= 1):
                            if(cur_board.grid[i][j].down == 0):
                                moves.append([i, j, 2])
        
        if(len(moves) > 0):
            rand = random.randint(0,len(moves) - 1)
            return moves[rand]
        
        else:
            for i in range(len(cur_board.grid)):
                for j in range(len(cur_board.grid)):
                    if cur_board.grid[i][j].up == 0:
                        moves.append( [i, j, 0])
                    elif cur_board.grid[i][j].right == 0:
                        moves.append( [i, j, 1])
                    elif cur_board.grid[i][j].down == 0:
                        moves.append( [i, j, 2])
                    elif cur_board.grid[i][j].left == 0:
                        moves.append( [i, j, 3])
            
        if(len(moves) > 0):
            rand = random.randint(0,len(moves) - 1)
            return moves[rand]
         
        return[-1, -1, -1]                
                    
    
    def boolean2int(b):
        if b:
            return 1
        else:
            return 0

    