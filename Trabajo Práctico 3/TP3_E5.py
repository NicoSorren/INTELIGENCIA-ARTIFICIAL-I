import random
import math

# Representación del tablero como una lista
def imprimir_tablero(tablero):
    for i in range(0, 9, 3):
        print(tablero[i:i+3])

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

# Función para el movimiento del jugador humano
def movimiento_humano(tablero):
    movimiento = int(input("Elige una posición (0-8): "))
    while tablero[movimiento] != ' ':
        movimiento = int(input("Posición inválida, elige otra: "))
    return movimiento

# Función para evaluar el estado del tablero
def evaluar(tablero, jugador):
    if verificar_ganador(tablero, jugador):
        return 10 if jugador == 'O' else -10
    elif verificar_empate(tablero):
        return 0
    else:
        return None  # No ha terminado el juego

# Movimiento del recocido simulado (IA)
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
        
        # Aceptar el nuevo movimiento si es mejor o con una probabilidad si es peor
        if nueva_puntuacion > mejor_puntuacion or random.random() < math.exp((nueva_puntuacion - mejor_puntuacion) / temperatura):
            mejor_movimiento = nuevo_movimiento
            mejor_puntuacion = nueva_puntuacion
        
        tablero_actual[nuevo_movimiento] = ' '  # Deshacer el movimiento temporal

    return mejor_movimiento

# Función principal del juego
def jugar_tateti():
    tablero = [' '] * 9
    turno = 'X'  # El humano comienza

    temp_inicial = float(input("Ingrese la temperatura inicial para la IA: "))
    
    while True:
        imprimir_tablero(tablero)
        
        if turno == 'X':  # Turno del humano
            movimiento = movimiento_humano(tablero)
        else:  # Turno de la IA
            movimiento = movimiento_recocido_simulado(tablero, temp_inicial)
            print(f"La IA elige la posición: {movimiento}")
        
        tablero[movimiento] = turno
        
        if verificar_ganador(tablero, turno):
            imprimir_tablero(tablero)
            print(f"¡{turno} ha ganado!")
            break
        elif verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break
        
        turno = 'O' if turno == 'X' else 'X'  # Cambiar de turno

# Ejecutar el juego
jugar_tateti()
