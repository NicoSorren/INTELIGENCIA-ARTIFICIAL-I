import heapq

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []
        self.costo = 1 if nombre != 'W' else 30  # Costo 1 para todas las casillas excepto 'W' que tiene costo 30

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        nodo = Nodo(nombre)
        self.nodos[nombre] = nodo
        return nodo

    def obtener_nodo(self, nombre):
        return self.nodos.get(nombre, None)

    def agregar_arista(self, desde, hasta):
        if desde in self.nodos and hasta in self.nodos:
            self.nodos[desde].agregar_vecino(self.nodos[hasta])

    def distancia_manhattan(self, nodo1, nodo2):
        # Supongamos que las coordenadas están basadas en la posición en la lista de nodos
        idx1 = nombres_nodos.index(nodo1.nombre)
        idx2 = nombres_nodos.index(nodo2.nombre)
        return abs(idx1 - idx2)

    def a_estrella(self, inicio, objetivo):
        # Inicializamos la cola de prioridad
        cola = []
        heapq.heappush(cola, (0, self.nodos[inicio], [inicio], 0))  # (f, nodo actual, camino, g)
        visitados = set()

        while cola:
            f_actual, nodo_actual, camino, g_actual = heapq.heappop(cola)

            if nodo_actual.nombre in visitados:
                continue

            visitados.add(nodo_actual.nombre)

            if nodo_actual.nombre == objetivo:
                return camino

            for vecino in sorted(nodo_actual.vecinos, key=lambda x: x.nombre):
                if vecino.nombre not in visitados:
                    g_nuevo = g_actual + vecino.costo
                    h = self.distancia_manhattan(vecino, self.nodos[objetivo])
                    f_nuevo = g_nuevo + h
                    heapq.heappush(cola, (f_nuevo, vecino, camino + [vecino.nombre], g_nuevo))

        return None

# Creación del grafo y los nodos
grafo = Grafo()

# Lista de nombres de los nodos según nuestro grafo
nombres_nodos = ['I', 'G', 'P', 'Q', 'R', 'T', 'W', 'K', 'M', 'N', 'E', 'F', 'C', 'A', 'B', 'D']

# Agregar cada nodo al grafo
for nombre in nombres_nodos:
    grafo.agregar_nodo(nombre)

# Agregando las aristas entre los nodos según nuestro grafo
grafo.agregar_arista('I', 'G')
grafo.agregar_arista('I', 'Q')
grafo.agregar_arista('I', 'W')
grafo.agregar_arista('G', 'P')
grafo.agregar_arista('P', 'Q')
grafo.agregar_arista('Q', 'R')
grafo.agregar_arista('Q', 'T')
grafo.agregar_arista('W', 'K')
grafo.agregar_arista('K', 'M')
grafo.agregar_arista('M', 'N')
grafo.agregar_arista('M', 'F')
grafo.agregar_arista('M', 'C')
grafo.agregar_arista('N', 'E')
grafo.agregar_arista('C', 'A')
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('B', 'D')

# Llamada a la función A* para encontrar el camino desde 'I' hasta 'F'
camino = grafo.a_estrella('I', 'F')

# Imprimir el camino encontrado, si lo hay
print("Camino encontrado:", camino)

import pygame
import time

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
PATH_COLOR = (0, 255, 0)  # Color verde para el camino

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

# Camino a animar (reemplaza con el camino real de tu algoritmo A*)
camino

# Función para obtener la posición de una letra en el tablero
def obtener_posicion(letra):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == letra:
                return (row, col)
    return None

# Bucle principal
running = True
animating = True
camino_recorrido = []

while running:
    window.fill(BLACK)

    # Dibujar el tablero con animación
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None:
                # Pintar de blanco inicialmente
                color = WHITE if (row, col) not in camino_recorrido else PATH_COLOR
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

    # Animación
    if animating and camino:
        current_node = camino.pop(0)
        pos = obtener_posicion(current_node)
        if pos:
            camino_recorrido.append(pos)
        time.sleep(0.5)  # Retraso para la animación (ajustar según sea necesario)

        if not camino:
            animating = False

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
