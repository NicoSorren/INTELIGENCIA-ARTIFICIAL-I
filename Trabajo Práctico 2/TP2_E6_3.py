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
