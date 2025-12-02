import pygame
import random

# --- Constantes ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

WIDTH = 300
HEIGHT = 600
ROWS = 20
COLS = 10
CELL_SIZE = WIDTH // COLS

COLORS = [
    (0, 255, 255),   # Cyan
    (0, 0, 255),     # Azul
    (255, 165, 0),   # Naranja
    (255, 255, 0),   # Amarillo
    (0, 255, 0),     # Verde
    (128, 0, 128),   # Morado
    (255, 0, 0)      # Rojo
]

# --- Formas de las piezas ---
# --- Formas de las piezas (cada forma dentro de una lista para sus rotaciones) ---
SHAPES = [
    [[[1, 1, 1, 1]]],  # I
    [[[1, 1, 1],
      [0, 1, 0]]],     # T
    [[[1, 1, 0],
      [0, 1, 1]]],     # S
    [[[0, 1, 1],
      [1, 1, 0]]],     # Z
    [[[1, 1],
      [1, 1]]],        # O
    [[[1, 0, 0],
      [1, 1, 1]]],     # L
    [[[0, 0, 1],
      [1, 1, 1]]]      # J
]


# --- Inicializar pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# --- Funciones ---
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if (col, row) in locked_positions:
                grid[row][col] = locked_positions[(col, row)]
    return grid

def draw_grid(surface, grid):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(surface, grid[row][col],
                             (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, GRAY,
                             (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        for j, column in enumerate(line):
            if column == 1:
                positions.append((shape.x + j, shape.y + i))
    return positions

def valid_space(shape, grid):
    accepted_pos = [[(c, r) for c in range(COLS) if grid[r][c] == BLACK] for r in range(ROWS)]
    accepted_pos = [pos for sub in accepted_pos for pos in sub]

    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] >= 0:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    return Piece(5, 0, random.choice(SHAPES))

def clear_rows(grid, locked):
    increment = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            increment += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if increment > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + increment)
                locked[newKey] = locked.pop(key)
    return increment

def draw_window(surface, grid):
    surface.fill(BLACK)
    draw_grid(surface, grid)
    pygame.display.update()

# --- Clase Piece ---
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)
        self.rotation = 0

# --- Juego principal ---
def main():
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    fall_time = 0
    fall_speed = 0.5

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)

        for pos in shape_pos:
            x, y = pos
            if y >= 0:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)

        draw_window(screen, grid)

        if check_lost(locked_positions):
            run = False
    pygame.display.quit()

# --- Ejecutar ---
main()
