import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuraciones básicas
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Configuración de pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(WHITE)

# Dibujar líneas del tablero
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Dibujar el tablero
draw_lines()

# Actualizar pantalla
pygame.display.update()

# Configuración inicial del juego
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 1  # 1: Jugador, -1: Máquina

# Funciones para dibujar X y O
def draw_x(row, col):
    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_asc, CROSS_WIDTH)
    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_desc, CROSS_WIDTH)

def draw_o(row, col):
    center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
    pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

# Función para marcar el tablero
def mark_square(row, col, player):
    board[row][col] = player
    if player == 1:
        draw_x(row, col)
    elif player == -1:
        draw_o(row, col)
    pygame.display.update()

# Función para verificar si alguien ha ganado
def check_win(player):
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False

# Función para verificar si hay empate
def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Función de costo para el recocido simulado
def evaluate_board():
    if check_win(-1):
        return -1  # La máquina gana
    if check_win(1):
        return 1  # El jugador gana
    return 0  # Empate o juego en progreso

# Función de vecindad para generar nuevos estados
def get_neighbors():
    neighbors = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                new_board = [row.copy() for row in board]
                new_board[row][col] = -1
                neighbors.append((row, col, new_board))
    return neighbors

# Función de recocido simulado
def simulated_annealing():
    current_temp = 100
    temp_min = 1
    cooling_rate = 0.99

    current_board = [row.copy() for row in board]
    current_cost = evaluate_board()

    while current_temp > temp_min:
        neighbors = get_neighbors()
        if not neighbors:
            break
        next_move, next_board = random.choice(neighbors)[:2]
        next_cost = evaluate_board()

        cost_diff = next_cost - current_cost

        if cost_diff < 0 or random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
            current_board = next_board
            current_cost = next_cost

        current_temp *= cooling_rate

    return next_move

# Lógica del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if board[clicked_row][clicked_col] is None:
                mark_square(clicked_row, clicked_col, 1)
                if check_win(1):
                    print("¡Felicidades! Ganaste.")
                    running = False
                elif check_draw():
                    print("¡Es un empate!")
                    running = False
                else:
                    player = -1  # Cambiar turno a la máquina

    if player == -1:
        machine_move = simulated_annealing()
        mark_square(machine_move[0], machine_move[1], -1)
        if check_win(-1):
            print("La máquina ganó.")
            running = False
        elif check_draw():
            print("¡Es un empate!")
            running = False
        player = 1  # Cambiar turno al jugador

# Finalizar Pygame
pygame.quit()
