# Clase Nodo representa cada nodo del grafo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del nodo (por ejemplo, 'I', 'F', etc.)
        self.vecinos = []  # Lista de nodos vecinos (conexiones)

    def agregar_vecino(self, vecino):
        # Método para agregar un nodo vecino a la lista de vecinos
        self.vecinos.append(vecino)


# Clase Grafo gestiona los nodos y las conexiones (aristas) entre ellos
class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos del grafo

    def agregar_nodo(self, nombre):
        # Método para crear un nuevo nodo y agregarlo al grafo
        nodo = Nodo(nombre)  # Crear un nodo con el nombre dado
        self.nodos[nombre] = nodo  # Agregar el nodo al diccionario de nodos
        return nodo  # Retornar el nodo creado

    def obtener_nodo(self, nombre):
        # Método para obtener un nodo del grafo por su nombre
        return self.nodos.get(nombre, None)  # Retorna el nodo si existe, sino None

    def agregar_arista(self, desde, hasta):
        # Método para conectar dos nodos en el grafo (agregar una arista)
        if desde in self.nodos and hasta in self.nodos:
            # Verificar que ambos nodos existen en el grafo
            self.nodos[desde].agregar_vecino(self.nodos[hasta])  # Agregar 'hasta' como vecino de 'desde'

    def dfs(self, inicio, objetivo):
        # Método para realizar la búsqueda en profundidad (DFS)
        
        # Inicializar la pila con una tupla que contiene el nodo inicial y el camino hasta él
        pila = [(self.nodos[inicio], [inicio])]
        visitados = set()  # Conjunto para rastrear los nodos ya visitados

        while pila:
            # Mientras haya nodos en la pila, continuar el proceso
            nodo_actual, camino = pila.pop()  # Extraer el último nodo de la pila y su camino

            if nodo_actual.nombre not in visitados:
                # Si el nodo actual no ha sido visitado, procesarlo
                visitados.add(nodo_actual.nombre)  # Marcar el nodo como visitado

                if nodo_actual.nombre == objetivo:
                    # Si el nodo actual es el objetivo, retornar el camino
                    return camino

                for vecino in nodo_actual.vecinos:
                    # Para cada vecino del nodo actual, agregarlo a la pila junto con el nuevo camino
                    pila.append((vecino, camino + [vecino.nombre]))

        return None  # Si no se encuentra el objetivo, retornar None


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

# Llamada a la función DFS para encontrar el camino desde 'I' hasta 'F'
camino = grafo.dfs('I', 'F')

# Imprimir el camino encontrado, si lo hay
print("Camino encontrado:", camino)
