BOARD = [
    [None, None, None, 0, 0, 0, 0, 0, None, None, None],
    [None, None, None, None, None, 0, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    [0, None, None, None, None, 1, None, None, None, None, 0],
    [0, None, None, None, 1, 1, 1, None, None, None, 0],
    [0, 0, None, 1, 1, 1, 1, 1, None, 0, 0],
    [0, None, None, None, 1, 1, 1, None, None, None, 0],
    [0, None, None, None, None, 1, None, None, None, None, 0],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 0, None, None, None, None, None],
    [None, None, None, 0, 0, 0, 0, 0, None, None, None],
]

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 11
CELL_SIZE = WIDTH // GRID_SIZE
BORDER_WIDTH = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BROWN = (210, 180, 140)
GRAY = (128, 128, 128)
OFF_WHITE = (255, 255, 240)
