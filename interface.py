"""
interface.py: sets up the board and helps players interact.
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


def setup_dots(GRID_SIZE):
    dots = []
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            dots.append(Dot(dot_blue, i * 74, j * 74))
    return dots


def main():
    game = setup()
    p1 = Player_One(0)
    p2 = Player_Two(0)

    curturn = 1  # whoever's turn it is
    num_filled = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # display dots and background
        cur_board = copy.deepcopy(game.boards[len(game.boards) - 1])
        screen.blit(background, (0, 0))
        for i in range(len(cur_board.grid) + 1):
            for j in range(len(cur_board.grid) + 1):
                d = Dot(dot_blue, i * 74, j * 74)
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
        triple = [None, None, None]
        if curturn == 1:
            triple = p1.move(game)
        else:
            assert curturn == 2, "It is not either of their turn??!"
            triple = p2.move(game)
        if triple[0] != -1:
            cur_board.fill_edge(triple[0], triple[1], triple[2], curturn)

        # update who's turn it is
        if num_filled != game.fill_count():  # if a square was filled in
            num_filled = game.fill_count()
            if curturn == 1:
                p1.score += 1
            else:
                p2.score += 1
        else:
            curturn = curturn % 2 + 1  # if a square wasn't filled, it's now the next person's turn
        pygame.display.update()
        game.boards.append(cur_board)
        time.sleep(1)
main()
