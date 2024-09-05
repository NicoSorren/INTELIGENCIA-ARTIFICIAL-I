import heapq
import matplotlib.pyplot as plt 
import numpy as np

# Armo el tablero, 1 casillas blancas 0 negras (12x14)
tablero = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

inicio = (2, 1)  # Posición de I (el (0,0) es la posición de la izq arriba, columna y fila 0)
fin = (10, 8)     # Posición de F

# Movimientos posibles
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para calcular la heurística (distancia de Manhattan)
def heuristica(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Función de búsqueda A*
def a_estrella(tablero, inicio, fin):
    filas, columnas = tablero.shape
    pq = [(0 + heuristica(inicio, fin), 0, inicio, [])]  #pq es una lista (heurística + costo, costo, nodo, camino)
    visitados = set() # crea un conjunto vacio, un ocnjunto es parecido a una lista pero mas rapido de acceder y no permite elemntos duplicados
    
    while pq:
        # la función heapq.heappop extrae el elemento de mayor prioridad (menro valor) y ese "elemento" es un nodo de la lista de forma  (heurística + costo, costo, nodo, camino)
        # para poder usar los valores de ese nodo los almaceno en variables (en la heuristica se pone _ porque no la necesito) 
        _, costo, nodo, camino = heapq.heappop(pq)
        
        if nodo in visitados:
            continue # si el nodo ya fue visitado el bucle while omite el resto del codigo y pasa a la siguiente iteración con otro nodo
        visitados.add(nodo)
        camino = camino + [nodo]
        
        if nodo == fin:
            return camino
        
        #voy a encontrar las coordenadas de los vecinos 
        for movimiento in movimientos:
            vecino = (nodo[0] + movimiento[0], nodo[1] + movimiento[1])
            
            #verifico que si se pueda (que este en los limites, no pase por los obstaculos)
            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas and tablero[vecino] == 1:
                nuevo_costo = costo + 1
                heur = nuevo_costo + heuristica(vecino, fin)
                #agrego el vecino a la lista de prioridad
                heapq.heappush(pq, (heur, nuevo_costo, vecino, camino))
    
    return []

# Encontrar el camino usando A*
camino = a_estrella(tablero, inicio, fin)
print("Camino encontrado por A*:", camino)

# Visualización del camino en el tablero
def mostrar_tablero(tablero, camino, inicio, fin):
    tablero_copy = np.zeros((tablero.shape[0], tablero.shape[1], 3))  # Crear un tablero en RGB(para poder poner colores, Red-Green-Blue)
    
    #pongo en blanco los 1 y en negro los 0
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if tablero[i, j] == 1:
                tablero_copy[i, j] = [1, 1, 1]  # Casillas en blanco
            else:
                tablero_copy[i, j] = [0, 0, 0]  # Obstáculos en negro
    
    for (x, y) in camino:
        tablero_copy[x, y] = [1, 1, 0]  # Camino en amarillo
    

    # Colores de las casillas de inicio y fin
    tablero_copy[inicio] = [0, 0, 1]  # Inicio en azul
    tablero_copy[fin] = [1, 0, 0]    # Fin en rojo
    
    # muevo las casillas para que arranquen de 0(si no por defecto las centra en los enteros, entonces la primera va de -0.5 a 0.5)
    plt.imshow(tablero_copy, extent=[0, tablero.shape[1], 0, tablero.shape[0]])

    #Agrego esto para que se vea la grilla (cuadriculas)
    plt.grid(True, color='black', linestyle='-', linewidth=1)
    # Acomodo el paso de la grilla para que coincida con las casillas "(inciio,fin, paso)"
    plt.xticks(np.arange(0, 13, 1))
    plt.yticks(np.arange(0, 15, 1))
    #saco los numeros de los ejes
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])

    plt.title("Camino encontrado por A*")
    plt.show()

mostrar_tablero(tablero, camino, inicio, fin)
