import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana y la cuadrícula
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Cambiar el rótulo de la ventana
pygame.display.set_caption("Hormiga ****")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crear una cuadrícula
grid_size = 100
cell_size = width // grid_size
grid = [[WHITE for _ in range(grid_size)] for _ in range(grid_size)]

# Posición inicial de la hormiga
x, y = random.randint(0, 50), random.randint(50, 50)
# Direcciones: arriba(0), derecha(1), abajo(2), izquierda(3)
direction = random.randint(0, 3)

# Definir movimientos
def turn_right():
    global direction
    direction = (direction + 1) % 4

def turn_left():
    global direction
    direction = (direction - 1) % 4

def move_forward():
    global x, y
    if direction == 0:
        y = (y - 1) % grid_size
    elif direction == 1:
        x = (x + 1) % grid_size
    elif direction == 2:
        y = (y + 1) % grid_size
    elif direction == 3:
        x = (x - 1) % grid_size

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cambiar color y girar
    if grid[y][x] == WHITE:
        grid[y][x] = BLACK
        turn_right()
    else:
        grid[y][x] = WHITE
        turn_left()
    
    # Mover hacia adelante
    move_forward()

    # Dibujar la cuadrícula
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, grid[i][j], (j * cell_size, i * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(10000000000000)

pygame.quit()
