import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
ANCHO_VENTANA, ALTO_VENTANA = 300, 300
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ta-te-ti con IA")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Tamaño del tablero
TAM_CELDA = 100
tablero = [' '] * 9

def dibujar_tablero():
    VENTANA.fill(BLANCO)
    for x in range(1, 3):
        pygame.draw.line(VENTANA, NEGRO, (x * TAM_CELDA, 0), (x * TAM_CELDA, ALTO_VENTANA), 2)
        pygame.draw.line(VENTANA, NEGRO, (0, x * TAM_CELDA), (ANCHO_VENTANA, x * TAM_CELDA), 2)
    
    # Dibujar las X y O
    for i in range(9):
        x = i % 3
        y = i // 3
        centro_x = x * TAM_CELDA + TAM_CELDA // 2
        centro_y = y * TAM_CELDA + TAM_CELDA // 2
        
        if tablero[i] == 'X':
            pygame.draw.line(VENTANA, ROJO, (centro_x - 20, centro_y - 20), (centro_x + 20, centro_y + 20), 2)
            pygame.draw.line(VENTANA, ROJO, (centro_x + 20, centro_y - 20), (centro_x - 20, centro_y + 20), 2)
        elif tablero[i] == 'O':
            pygame.draw.circle(VENTANA, AZUL, (centro_x, centro_y), 30, 2)

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]  # diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in combinacion):
            return True
    return False

def verificar_empate(tablero):
    return all(casilla != ' ' for casilla in tablero)

def movimiento_humano(tablero, pos):
    fila = pos[1] // TAM_CELDA
    columna = pos[0] // TAM_CELDA
    return fila * 3 + columna

def movimiento_recocido_simulado(tablero, temp_inicial):
    tablero_actual = tablero[:]
    movimiento_actual = random.choice([i for i in range(9) if tablero[i] == ' '])
    mejor_movimiento = movimiento_actual
    mejor_puntuacion = -float('inf')
    temperatura = temp_inicial

    for paso in range(100):  # Número máximo de iteraciones
        temperatura *= 0.99  # Enfriamiento
        if temperatura < 0.01:
            break

        nuevo_movimiento = random.choice([i for i in range(9) if tablero[i] == ' '])
        tablero_actual[nuevo_movimiento] = 'O'
        nueva_puntuacion = evaluar(tablero_actual, 'O')

        if nueva_puntuacion is None:  # Si no se terminó el juego, resetear
            nueva_puntuacion = 0

        if nueva_puntuacion > mejor_puntuacion or random.random() < math.exp((nueva_puntuacion - mejor_puntuacion) / temperatura):
            mejor_movimiento = nuevo_movimiento
            mejor_puntuacion = nueva_puntuacion

        tablero_actual[nuevo_movimiento] = ' '  # Deshacer el movimiento temporal

    return mejor_movimiento

def evaluar(tablero, jugador):
    if verificar_ganador(tablero, jugador):
        return 10 if jugador == 'O' else -10
    elif verificar_empate(tablero):
        return 0
    else:
        return None

def main():
    turno = 'X'

    # Pedir la temperatura inicial antes de iniciar el juego
    temp_inicial = float(input("Ingrese la temperatura inicial para la IA: "))
    
    jugando = True
    ganador = None

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and turno == 'X':
                pos = pygame.mouse.get_pos()
                movimiento = movimiento_humano(tablero, pos)
                if tablero[movimiento] == ' ':
                    tablero[movimiento] = 'X'
                    if verificar_ganador(tablero, 'X'):
                        ganador = 'X'
                        jugando = False
                    elif verificar_empate(tablero):
                        ganador = 'Empate'
                        jugando = False
                    turno = 'O'
        
        if turno == 'O' and jugando:
            pygame.time.wait(500)  # Añadir un pequeño retraso para el turno de la IA
            movimiento = movimiento_recocido_simulado(tablero, temp_inicial)
            tablero[movimiento] = 'O'
            if verificar_ganador(tablero, 'O'):
                ganador = 'O'
                jugando = False
            elif verificar_empate(tablero):
                ganador = 'Empate'
                jugando = False
            turno = 'X'
        
        dibujar_tablero()
        pygame.display.update()

    print(f"Ganador: {ganador}")
    pygame.quit()

main()
