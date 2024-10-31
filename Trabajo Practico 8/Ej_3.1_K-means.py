import numpy as np 
import matplotlib.pyplot as plt

n=23

x=np.random.uniform(0, 5, n)
y=np.random.uniform(0, 5, n)

#graficos
plt.scatter(x, y, color='blue')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Conjunto de 23 Puntos Aleatorios')
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid(True)
plt.show()


