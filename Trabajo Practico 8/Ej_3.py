import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
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

# Ejecutar K-means con k=2
k_means_clusters = 2
centros_finales, etiquetas_finales = ejecutar_kmeans(datos, centros_iniciales, k_means_clusters)

# Graficar los resultados de K-means
plt.figure(figsize=(8, 6))
colores_clusters = np.array(['blue', 'green'])
plt.scatter(datos[etiquetas_finales == 0, 0], datos[etiquetas_finales == 0, 1], c='blue', label='Grupo 1 (K-means)')
plt.scatter(datos[etiquetas_finales == 1, 0], datos[etiquetas_finales == 1, 1], c='green', label='Grupo 2 (K-means)')
plt.scatter(centros_finales[:, 0], centros_finales[:, 1], color='red', marker='x', s=100, label="Centros Finales")
plt.title('Clusters obtenidos con K-means')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Iteración en diferentes valores de K en KNN y graficar cada uno por separado
for K in range(1, 9, 2):
    knn = KNeighborsClassifier(n_neighbors=K)
    knn.fit(datos, etiquetas_finales)
    etiquetas_nuevos_datos = knn.predict(nuevos_datos)
    
    # Asignación de colores a los puntos restantes basados en los grupos de K-means
    colores_nuevos = colores_clusters[etiquetas_nuevos_datos]
    
    # Gráfica de los puntos restantes con la clasificación de KNN
    plt.figure(figsize=(8, 6))
    plt.scatter(datos[etiquetas_finales == 0, 0], datos[etiquetas_finales == 0, 1], c='blue', label='Grupo 1 (K-means)')
    plt.scatter(datos[etiquetas_finales == 1, 0], datos[etiquetas_finales == 1, 1], c='green', label='Grupo 2 (K-means)')
    plt.scatter(nuevos_datos[:, 0], nuevos_datos[:, 1], c=colores_nuevos, edgecolor='black', s=100, label='Puntos Clasificados (KNN)')
    
    plt.title(f'Clasificación KNN con K={K}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
