import numpy as np

# Definición de parámetros
num_salas = 6
num_episodios = 1000
tasa_aprendizaje = 1 ##Por la fórmula que utilizamos para el cálculo de Q se considera 1 (Q=R + Y max(Q), se puede modificar y aplicar la fórmula general)
factor_descuento = 0.9
epsilon = 0.2

# Definición de la matriz de recompensas R
R = np.array([
    [-10, 0, -10, 0, -10, -10],
    [0, -10, 0, -10, -10, -10],
    [-10, 0, -10, 0, -10, 100],
    [0, -10, 0, -10, 0, -10],
    [-10, -10, -10, 0, -10, 100],
    [-10, -10, 0, -10, 0, 100]
])

# Inicialización de la matriz Q con ceros
Q = np.zeros((num_salas, num_salas))

# Función para elegir una acción dando un 20% de probabilidad de hacer movimientos aleatorios, de lo contrario
# lleva a cabo la acción que maximice Q.
def seleccionar_accion(estado):
    if np.random.rand() < epsilon:
        return np.random.choice(num_salas)
    else:
        return np.argmax(Q[estado, :])

# Ciclo de entrenamiento
for episodio in range(num_episodios):
    estado_actual = np.random.randint(0, num_salas)
    while estado_actual != 5:  # La meta es llegar a la Sala 6
        accion = seleccionar_accion(estado_actual)
        estado_siguiente = accion
        recompensa = R[estado_actual, accion]      
        Q[estado_actual, accion] = Q[estado_actual, accion] + tasa_aprendizaje * (recompensa + factor_descuento * np.max(Q[estado_siguiente, :]) - Q[estado_actual, accion])
        estado_actual = estado_siguiente

# Impresión de la matriz Q (valores finales)
print("Matriz Q:")
print(Q)

# Normalización de la matriz Q
Q_max = np.max(Q)
Q_normalized = Q / Q_max

# Impresión de la matriz Q normalizada
print("Matriz Q normalizada:")
print(Q_normalized)

# Selección del camino óptimo desde la Sala 1 (estado 0) a la Sala 6 (estado 5)
estado_actual = 0
camino = [estado_actual]
while estado_actual != 5:
    accion = np.argmax(Q[estado_actual, :])
    estado_actual = accion
    camino.append(estado_actual)

print("Camino óptimo:", camino)



