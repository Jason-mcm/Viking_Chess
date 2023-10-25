from piece import *
import pygame


class Board:

    def __init__(self, window):
        self.board = BOARD
        self.selected_piece = None
        self.window = window
        self.pieces = []
        self.draw_board()

    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = LIGHT_BROWN
                if self.board[row][col] == 0:
                    color = GRAY
                elif self.board[row][col] == 1:
                    color = OFF_WHITE
                pygame.draw.rect(self.window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(self.window, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                                 BORDER_WIDTH)

    def draw_pieces(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    piece = Piece(row, col, BLACK)
                    self.pieces.append(piece)
                    piece.draw(self.window)
                elif self.board[row][col] == 1:
                    piece = Piece(row, col, WHITE)
                    self.pieces.append(piece)
                    piece.draw(self.window)
