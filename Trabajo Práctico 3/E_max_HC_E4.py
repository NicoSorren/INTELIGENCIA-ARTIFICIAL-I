"""Encontrar el Maximo _hill climbing_"""
import numpy
import numpy as np

# Definir el dominio
x_values = np.linspace(-10, -6, 40)  # 40 puntos en el rango [-10, -6] (-10+6= -4)--> (-4/0.1=40)

# Definir la función f(x)
def f(x):
    return np.sin(x) / (x + 0.1)

# Crear el vector de valores de la función
function = f(x_values)

# Imprimir el vector
print(function)

def maximo(a):
    max = a[0]
    l = len(a)
    for i in range(1, l):
        max1 = a[i]
        if max <= max1:
            max = max1
    print("Valor maximo:", max)

maximos = maximo(function)
