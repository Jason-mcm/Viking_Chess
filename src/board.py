from piece import *
import pygame
import sys


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

    def init_pieces(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    piece = Piece(row, col, BLACK)
                    self.pieces.append(piece)
                    # piece.draw(self.window)
                elif self.board[row][col] == 1:
                    piece = Piece(row, col, WHITE)
                    self.pieces.append(piece)
                    # piece.draw(self.window)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    print("left moust clicked")
                    x, y = event.pos
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE

                    # Check if a piece is selected
                    for piece in self.pieces:
                        if piece.row == row and piece.col == col:
                            self.selected_piece = piece

                elif event.button == 3:  # Right mouse button clicked
                    print("Right clicked")
                    if self.selected_piece:
                        x, y = event.pos
                        col = x // CELL_SIZE
                        row = y // CELL_SIZE

                        # Check if the move is valid and move the piece
                        piece = Piece(0, 0, RED)
                        piece.draw(self.window)
                        piece.move(10, 10)
                        piece.draw(self.window)
                        self.selected_piece.move(row, col)
                        self.selected_piece = None


    def update(self):
        self.handle_events()

    def draw_pieces(self):
        self.init_pieces()
        for piece in self.pieces:
            piece.draw(self.window)

    def run(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.window.fill(BLACK)  # Clear the screen
            self.draw_board()
            self.draw_pieces()
            pygame.display.update()
            clock.tick(30)  # Limit the frame rate

        pygame.quit()
        sys.exit()