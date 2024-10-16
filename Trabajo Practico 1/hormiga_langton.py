import matplotlib.pyplot as plt
import numpy as np

# Definimos una clase para la Hormiga
class Hormiga:
    def __init__(self, x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion  # 0: Arriba, 1: Derecha, 2: Abajo, 3: Izquierda

    def girar_derecha(self):
        self.direccion = (self.direccion + 1) % 4           # % 4 se utiliza para asegurar la dirección se mantenga entre 0 y 3
    # Si estamos por ejemplo en 0 (arriba) quiero que rote en sentido de agujas de reloj. Es decir, quiero que valga 1.

    def girar_izquierda(self):
        self.direccion = (self.direccion - 1) % 4
    # Si estamos por ejemplo en 1 (derecha) quiero que rote en sentido contrario de agujas de reloj. Es decir, quiero que valga 0.
    def mover(self):
        # en este sistema x es positivo derecha. y es positivo hacia abjo
        if self.direccion == 0:  # Arriba
            self.y -= 1             # si va hacia arriba se reduce coordenada y en 1.
        elif self.direccion == 1:  # Derecha
            self.x += 1
        elif self.direccion == 2:  # Abajo
            self.y += 1
        elif self.direccion == 3:  # Izquierda
            self.x -= 1

# Definimos una clase para la Cuadrícula
class Cuadricula:
    def __init__(self, tamaño):
        self.tamaño = tamaño                                    # parametro tamaño sale de instancia cuadricula en ejecutar_experimento
        self.celdas = np.zeros((tamaño, tamaño), dtype=int)     # Se crea matriz de ceros de tipo de datos entero. 

    def invertir_color(self, x, y):
        self.celdas[y, x] = 1 - self.celdas[y, x]               # si celda donde se accede valor es 0 (blanca), entonces 1-0 dando 1 como resultado cambia color a negra

    def color_celda(self, x, y):
        return self.celdas[y, x]            # consulta estado de celda antes de realizar acción

    def mostrar(self):
        plt.imshow(self.celdas, cmap='binary')
        plt.axis('off')
        plt.show()

# Función para ejecutar el experimento de la hormiga de Langton
def ejecutar_experimento(tamaño, iteraciones):
    cuadricula = Cuadricula(tamaño)     # Se crea instancia de clase 'Cuadricula' con tamaño especificaod
    hormiga = Hormiga(tamaño // 2, tamaño // 2, 0)      # Se crea instancia de clase 'Hormiga'. Con calculos que salen ahi hacemos que hormiga inicie en centro de cuadricula
                                                        # Hacemos que movimiento inicial sea hacia arriba
                                                        
    for _ in range(iteraciones):        # _ se usa porque es una variable que no utilizamos dentro de bucle
        if cuadricula.color_celda(hormiga.x, hormiga.y) == 0:  # Celda blanca
            cuadricula.invertir_color(hormiga.x, hormiga.y)
            hormiga.girar_derecha()
        else:  # Celda negra
            cuadricula.invertir_color(hormiga.x, hormiga.y)
            hormiga.girar_izquierda()
        hormiga.mover()

        # Asegurarse de que la hormiga permanece dentro de la cuadrícula
        hormiga.x = hormiga.x % tamaño
        hormiga.y = hormiga.y % tamaño

    cuadricula.mostrar()

# Ejecutar el experimento con una cuadrícula de 101x101 y 11000 iteraciones
ejecutar_experimento(101, 11000)
