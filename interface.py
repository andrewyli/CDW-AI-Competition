"""
interface.py: sets up the board and helps players interact.
DO NOT EDIT UNLESS INSTRUCTED TO
"""
from board import Board
from game import Game
from box import Box
from dot import Dot
from edge import Edge
from player_one import Player_One
from player_two import Player_Two

import sys
import time
import copy
import pygame
from pygame.locals import *


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)
GRID_SIZE = 8  # side length in terms of lines, not dots

background = pygame.image.load("Graphics/background.png")
dot_red = pygame.image.load("Graphics/dot_red.png")
dot_blue = pygame.image.load("Graphics/dot_blue.png")
horizontal_red = pygame.image.load("Graphics/horizontal_red.png")
vertical_red = pygame.image.load("Graphics/vertical_red.png")
horizontal_blue = pygame.image.load("Graphics/horizontal_blue.png")
vertical_blue = pygame.image.load("Graphics/vertical_blue.png")


def setup():  # creates the game
    grid = [[Box(0, 0, 0, 0) for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    boards = []
    boards.append(Board(grid))
    return Game(boards)


def setup_dots():
    dots = []
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            dots.append(Dot(dot_blue, i * 74, j * 74))
    return dots


def game_end(game, p1, p2):
    print "---------Final Score---------"
    print "P1: " + str(p1.score)
    print "P2: " + str(p2.score)
    sys.exit()


def main():
    game = setup()
    dots = setup_dots()
    p1 = Player_One(0)
    p2 = Player_Two(0)

    curturn = 1  # whoever's turn it is
    turns = 0
    while turns < 2 * GRID_SIZE * (GRID_SIZE + 1):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # display dots and background
        cur_board = copy.deepcopy(game.boards[len(game.boards) - 1])
        screen.blit(background, (0, 0))
        for d in dots:
            screen.blit(d.image, d.rect)

        # check to see which edges should be displayed
        for i in range(len(cur_board.grid)):
            for j in range(len(cur_board.grid)):
                e1 = Dot(dot_blue, 0, 0)
                e2 = Dot(dot_blue, 0, 0)
                e3 = Dot(dot_blue, 0, 0)
                e4 = Dot(dot_blue, 0, 0)
                if cur_board.grid[i][j].left == 1:
                    e1 = Edge(vertical_blue, i * 74 + 1, j * 74 + 11)
                elif cur_board.grid[i][j].left == 2:
                    e1 = Edge(vertical_red, i * 74 + 1, j * 74 + 11)
                if cur_board.grid[i][j].right == 1:
                    e2 = Edge(vertical_blue, (i + 1) * 74 + 1, j * 74 + 11)
                elif cur_board.grid[i][j].right == 2:
                    e2 = Edge(vertical_red, (i + 1) * 74 + 1, j * 74 + 11)
                if cur_board.grid[i][j].up == 1:
                    e3 = Edge(horizontal_blue, i * 74 + 11, j * 74 + 1)
                elif cur_board.grid[i][j].up == 2:
                    e3 = Edge(horizontal_red, i * 74 + 11, j * 74 + 1)
                if cur_board.grid[i][j].down == 1:
                    e4 = Edge(horizontal_blue, i * 74 + 11, (j + 1) * 74 + 1)
                elif cur_board.grid[i][j].down == 2:
                    e4 = Edge(horizontal_red, i * 74 + 11, (j + 1) * 74 + 1)
                screen.blit(e1.image, e1.rect)
                screen.blit(e2.image, e2.rect)
                screen.blit(e3.image, e3.rect)
                screen.blit(e4.image, e4.rect)

        # move
        triple = [-1, -1, -1]
        if curturn == 1:
            triple = p1.move(game)
        else:
            assert curturn == 2, "It is not either of their turn (somehow)!"
            triple = p2.move(game)
        if triple[0] != -1:
            cur_board.fill_edge(triple[0], triple[1], triple[2], curturn)
        
        box = False
        for i in range(len(cur_board.grid)):
            for j in range(len(cur_board.grid)):
                if(i > 0):          #this massive block is to make sure it counts squares right (hint: it still doesn't)
                    le = (cur_board.grid[i][j].left != 0 or cur_board.grid[i - 1][j].right != 0)
                else:
                    le = (cur_board.grid[i][j].left != 0)
                if(j < len(cur_board.grid) - 1):
                    do = (cur_board.grid[i][j].down != 0 or cur_board.grid[i][j + 1].up != 0)
                else:
                    do = (cur_board.grid[i][j].down != 0)
                if(i < len(cur_board.grid) - 1):
                    ri = (cur_board.grid[i][j].right != 0 or cur_board.grid[i + 1][j].left != 0)
                else:
                    ri = (cur_board.grid[i][j].right != 0)
                if(j > 0):
                    up = (cur_board.grid[i][j].up != 0 or cur_board.grid[i][j - 1].down != 0)
                else:
                    up = (cur_board.grid[i][j].up != 0)
                if le and do and ri and up and cur_board.grid[i][j].filled == False:  
                    # if a square was filled in this turn
                    cur_board.grid[i][j].filled = True
                    if (curturn == 1): 
                        p1.score += 1
                    if(curturn == 2):
                        p2.score += 1
                    
                    box = True
                    
        if not box:
            curturn = curturn % 2 + 1  # if a square wasn't filled, it's now the next person's turn
        pygame.display.update()
        game.boards.append(cur_board)
        time.sleep(0.01)
        turns += 1
        
    # game_end function
    game_end(game, p1, p2)
main()
