import numpy as np
import matplotlib.pyplot as plt
import time

# Establecer semilla para la reproducibilidad
np.random.seed(int(time.time()))

# Generar puntos aleatorios
datos = np.random.rand(20, 2) * 5
idx_centros_iniciales = np.random.choice(datos.shape[0], 2, replace=False)
centros_iniciales = datos[idx_centros_iniciales]

# Función para asignar puntos a los centros más cercanos
def asignar_a_centros(datos, centros):
    etiquetas = []
    for punto in datos:
        distancias = [np.sqrt(np.sum((punto - centro) ** 2)) for centro in centros]
        etiquetas.append(np.argmin(distancias))
    return np.array(etiquetas)

# Función para recalcular los centros
def recalcular_centros(datos, etiquetas, centros):
    nuevos_centros = []
    for i in range(len(centros)):
        puntos_del_grupo = datos[etiquetas == i]
        nuevos_centros.append(puntos_del_grupo.mean(axis=0) if len(puntos_del_grupo) > 0 else centros[i])
    return np.array(nuevos_centros)

# Implementación de K-means
def ejecutar_kmeans(datos, centros_iniciales, num_clusters):
    if num_clusters > len(centros_iniciales):
        nuevos_centros = datos[np.random.choice(datos.shape[0], num_clusters - len(centros_iniciales), replace=False)]
        centros = np.vstack([centros_iniciales, nuevos_centros])
    else:
        centros = centros_iniciales[:num_clusters]
    
    max_iteraciones = 100
    for _ in range(max_iteraciones):
        etiquetas = asignar_a_centros(datos, centros)
        nuevos_centros = recalcular_centros(datos, etiquetas, centros)
        if np.all(nuevos_centros == centros):
            break
        centros = nuevos_centros

    return centros, etiquetas

# Generar puntos adicionales
nuevos_datos = np.random.rand(3, 2) * 5

# Ejecutar K-means y graficar resultados para diferentes valores de k
for k_actual in [2, 3, 5]:
    centros_finales, etiquetas_finales = ejecutar_kmeans(datos, centros_iniciales, k_actual)
    etiquetas_nuevos_datos = asignar_a_centros(nuevos_datos, centros_finales)
    
    colores_clusters = plt.cm.viridis(np.linspace(0, 1, k_actual))
    colores_nuevos = plt.cm.plasma(np.linspace(0.3, 0.7, k_actual))

    plt.figure(figsize=(8, 6))
    for i in range(k_actual):
        puntos_cluster = datos[etiquetas_finales == i]
        plt.scatter(puntos_cluster[:, 0], puntos_cluster[:, 1], color=colores_clusters[i], label=f"Cluster {i+1}")

        nuevos_puntos_cluster = nuevos_datos[etiquetas_nuevos_datos == i]
        plt.scatter(nuevos_puntos_cluster[:, 0], nuevos_puntos_cluster[:, 1], color=colores_nuevos[i], edgecolor='black', label=f"Nuevos Cluster {i+1}")

    plt.scatter(centros_finales[:, 0], centros_finales[:, 1], color='red', marker='x', s=100, label="Centros Finales")

    plt.title(f"K-means con k={k_actual}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


