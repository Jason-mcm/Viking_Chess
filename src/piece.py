from constants import *
import pygame


class Piece:

    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = CELL_SIZE * self.col + CELL_SIZE // 2
        self.y = CELL_SIZE * self.row + CELL_SIZE // 2

    def draw(self, window):
        radius = CELL_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()
