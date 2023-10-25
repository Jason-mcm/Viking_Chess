import sys
from board import Board
from piece import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    running = True
    board = Board(WINDOW)
    board.draw_pieces()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
