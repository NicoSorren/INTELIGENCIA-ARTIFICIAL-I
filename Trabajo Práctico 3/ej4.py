import numpy as np

# definimos función
def f(x):
    return np.sin(x)/ (x+0.1)

# Discretizar dominio en intervalo [-10; -6] con pasos de 0.1
x_values = np.arange(-10, -6, 0.1)      # con arange generamos lista de puntos discretizadis

# inicializamos algoritmo seleccionado un punto aleatorio del intervalo
current_x = np.random.choice(x_values)  # random.choice devuelve un valor aleatorio extraído de la secuencia pasada como argumento
current_f = f(current_x)    # calculamos valor de función en ese punto

# definimos paso para moverse a los vecinos (discretización de 0.1)
step = 0.1

# comienza algortimo de Hill Climbing
while True:
    # Definir los vecinos a la izquierda y derecha
    left_x = current_x - step
    rigth_x = current_x + step

    # asegurarse de que vecinos no se exceden de intervalo
    if left_x < -10:
        left_x = -10
    if rigth_x > -6:
        rigth_x = -6
    
    # Calcular valor de la función en vecinos
    left_f = f(left_x)
    rigth_f = f(rigth_x)

    # Comparar valor actual con vecinos
    if current_f >= left_f and current_f >= rigth_f:
        break       # hemos encontrado el Máximo Local
    elif left_f > current_f:
        current_x = left_x
        current_f =left_f
    else:
        current_x = rigth_x
        current_f = rigth_f

# Imprimir resultado final
print(f"El máximo de la función es {current_f:.3f} \npara un valor de x igual a {current_x:.3f}")