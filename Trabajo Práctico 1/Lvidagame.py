import pygame
import numpy as np

# Configuración inicial
width, height = 500, 550
cell_size = 10
cols, rows = width // cell_size, height // cell_size

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de la Vida de Conway")

# Crear la cuadrícula inicial
grid = np.zeros((cols, rows))

# Llenar aleatoriamente algunas células para empezar
grid[10, 10] = 1
grid[11, 10] = 1
grid[12, 10] = 1
grid[12, 11] = 1
grid[11, 12] = 1

grid[10, 40] = 1
grid[11, 40] = 1
grid[12, 40] = 1
grid[12, 41] = 1
grid[11, 42] = 1

grid[5, 10] = 1
grid[6, 11] = 1
grid[7, 10] = 1
grid[7, 10] = 1
grid[6, 12] = 1

grid[25, 10] = 1
grid[26, 11] = 1
grid[27, 10] = 1
grid[27, 10] = 1
grid[26, 12] = 1

grid[10, 50] = 1
grid[11, 50] = 1
grid[12, 50] = 1
grid[12, 51] = 1
grid[11, 52] = 1

grid[5, 15] = 1
grid[6, 16] = 1
grid[7, 15] = 1
grid[7, 15] = 1
grid[6, 17] = 1

# Función para calcular el próximo estado de la cuadrícula
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(cols):
        for j in range(rows):
            # Contar las células vecinas vivas
            neighbors = int(grid[i, (j-1) % rows] + grid[i, (j+1) % rows] +
                            grid[(i-1) % cols, j] + grid[(i+1) % cols, j] +
                            grid[(i-1) % cols, (j-1) % rows] + grid[(i-1) % cols, (j+1) % rows] +
                            grid[(i+1) % cols, (j-1) % rows] + grid[(i+1) % cols, (j+1) % rows])

            # Aplicar las reglas
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el estado de la cuadrícula
    grid = update_grid(grid)

    # Dibujar la cuadrícula
    screen.fill((0, 0, 0))
    for i in range(cols):
        for j in range(rows):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (i * cell_size, j * cell_size, cell_size, cell_size))

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
