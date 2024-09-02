import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
width, height = 300, 300  # Ajusta según sea necesario
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tablero')

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Definir el tamaño de cada celda
cell_size = 50

# Crear una fuente para los textos
font = pygame.font.SysFont(None, 30)

# Definir la estructura del tablero
board = [
    [None, None, None, 'A', 'B', None],
    [None, None, None, 'C', 'D', 'E'],
    ['G', 'I', 'W', 'K', 'M', 'N'],
    ['P', 'Q', 'R', 'T', 'F', None]
]

# Definir colores de las celdas
cell_colors = [
    [None, None, None, WHITE, WHITE, WHITE],
    [None, None, None, WHITE, WHITE, None],
    [WHITE, YELLOW, WHITE, WHITE, WHITE, WHITE],
    [WHITE, WHITE, WHITE, WHITE, YELLOW, None]
]

# Definir las líneas rojas como separadores entre las celdas
red_lines = [
    # Línea entre C y D bien
    ((1, 3), (1, 4)),
    # Línea entre T y F (bien)
    ((3, 3), (3, 4)),
    # Línea entre D y E bien
    ((1, 4), (1, 5)),
    # Línea entre W y R 
    ((3, 2), (4, 2))
]

# Bucle principal
running = True
while running:
    window.fill(BLACK)

    # Dibujar el tablero
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None:
                color = cell_colors[row][col] if cell_colors[row][col] is not None else WHITE
                pygame.draw.rect(window, color, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
                text = font.render(board[row][col], True, BLACK)
                text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                window.blit(text, text_rect)

    # Dibujar las líneas rojas como separadores
    for line in red_lines:
        start_cell, end_cell = line

        if start_cell[0] == end_cell[0]:  # Si la línea es horizontal
            start_pos = (end_cell[1] * cell_size, start_cell[0] * cell_size)
            end_pos = (end_cell[1] * cell_size, (start_cell[0] + 1) * cell_size)
        else:  # Si la línea es vertical
            start_pos = (start_cell[1] * cell_size, start_cell[0] * cell_size)
            end_pos = ((start_cell[1] + 1) * cell_size, start_cell[0] * cell_size)

        pygame.draw.line(window, RED, start_pos, end_pos, 5)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
