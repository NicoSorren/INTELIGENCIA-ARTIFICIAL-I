import random

# Clase que representa una caja con su precio y peso
class Caja:
    def __init__(self, id, precio, peso):
        self.id = id
        self.precio = precio
        self.peso = peso

# Clase que representa un individuo con un conjunto de cajas (genotipo) y los métodos para evaluarlo
class Individuo:
    def __init__(self, cajas, max_peso):
        self.cajas = cajas  # Lista de cajas disponibles
        self.genotipo = [random.randint(0, 1) for _ in range(len(cajas))]  # Representación binaria del individuo
        self.max_peso = max_peso  # Peso máximo permitido para la grúa
        self.precio_total = 0
        self.peso_total = 0
        self.evaluar()  # Evalúa el individuo al crearlo

    # Evalúa el individuo calculando el precio total y el peso total del conjunto de cajas seleccionadas
    def evaluar(self):
        """Calcula el precio y el peso total del individuo"""
        self.precio_total = sum(caja.precio for i, caja in enumerate(self.cajas) if self.genotipo[i] == 1)
        self.peso_total = sum(caja.peso for i, caja in enumerate(self.cajas) if self.genotipo[i] == 1)
        if self.peso_total > self.max_peso:  # Penalización si excede el peso máximo permitido
            self.precio_total = 0  # Se pone el precio en 0 si el peso excede el límite

    # Verifica si el peso total es válido, es decir, no excede el máximo permitido
    def es_valido(self):
        return self.peso_total <= self.max_peso

# Clase que representa una población de individuos y maneja la evolución
class Poblacion:
    def __init__(self, cajas, max_peso, tam_poblacion):
        self.cajas = cajas
        self.max_peso = max_peso
        self.tam_poblacion = tam_poblacion
        self.individuos = [Individuo(cajas, max_peso) for _ in range(tam_poblacion)]  # Genera la población inicial
        self.mejor_individuo = None

    # Método de selección por ruleta para elegir individuos según su fitness
    def seleccionar_ruleta(self):
        """Selecciona individuos para la reproducción usando el método de la ruleta"""
        total_precio = sum(ind.precio_total for ind in self.individuos)
        if total_precio == 0:
            return random.choices(self.individuos, k=2)  # Selección aleatoria si todos tienen fitness 0
        seleccion = []
        for _ in range(self.tam_poblacion // 2):  # Selección de N/2 parejas
            ruleta = random.uniform(0, total_precio)
            acumulado = 0
            for ind in self.individuos:
                acumulado += ind.precio_total
                if acumulado >= ruleta:
                    seleccion.append(ind)
                    break
        return seleccion

    # Método que cruza dos individuos para generar dos descendientes
    def cruzar(self, padre1, padre2):
        """Cruza dos individuos usando un punto de cruce"""
        punto_cruce = random.randint(1, len(self.cajas) - 1)  # Se elige un punto de cruce al azar
        hijo1_genotipo = padre1.genotipo[:punto_cruce] + padre2.genotipo[punto_cruce:]
        hijo2_genotipo = padre2.genotipo[:punto_cruce] + padre1.genotipo[punto_cruce:]
        hijo1 = Individuo(self.cajas, self.max_peso)
        hijo2 = Individuo(self.cajas, self.max_peso)
        hijo1.genotipo = hijo1_genotipo
        hijo2.genotipo = hijo2_genotipo
        hijo1.evaluar()  # Recalcula los valores del nuevo individuo
        hijo2.evaluar()
        return hijo1, hijo2

    # Método que aplica la mutación con cierta probabilidad
    def mutar(self, individuo, prob_mutacion=0.1):
        """Aplica mutación a un individuo con cierta probabilidad"""
        for i in range(len(individuo.genotipo)):
            if random.random() < prob_mutacion:  # Si la probabilidad de mutación se cumple
                individuo.genotipo[i] = 1 - individuo.genotipo[i]  # Se invierte el gen (0 -> 1 o 1 -> 0)
        individuo.evaluar()  # Se evalúa de nuevo el individuo tras la mutación

    # Método principal que evoluciona la población durante un número de generaciones
    def evolucionar(self, generaciones, prob_mutacion=0.1):
        """Evoluciona la población a través de varias generaciones"""
        for generacion in range(generaciones):
            nueva_poblacion = []
            seleccionados = self.seleccionar_ruleta()  # Se seleccionan individuos mediante la ruleta

            # Asegurarse de que siempre hay un número par de seleccionados
            if len(seleccionados) % 2 != 0:
                seleccionados.append(random.choice(self.individuos))  # Si es impar, se añade uno al azar

            # Cruce de los seleccionados para generar descendientes
            for i in range(0, len(seleccionados), 2):
                padre1, padre2 = seleccionados[i], seleccionados[i + 1]
                hijo1, hijo2 = self.cruzar(padre1, padre2)
                self.mutar(hijo1, prob_mutacion)  # Se aplica la mutación a los hijos
                self.mutar(hijo2, prob_mutacion)
                if hijo1.es_valido():
                    nueva_poblacion.append(hijo1)  # Solo se añaden hijos válidos (que no superen el peso máximo)
                if hijo2.es_valido():
                    nueva_poblacion.append(hijo2)

            # Completamos la población si no hay suficientes individuos válidos
            while len(nueva_poblacion) < self.tam_poblacion:
                nuevo_individuo = Individuo(self.cajas, self.max_peso)
                if nuevo_individuo.es_valido():
                    nueva_poblacion.append(nuevo_individuo)

            self.individuos = nueva_poblacion

            # Encontrar el mejor individuo de esta generación
            mejor_individuo = max(self.individuos, key=lambda ind: ind.precio_total)
            if self.mejor_individuo is None or mejor_individuo.precio_total > self.mejor_individuo.precio_total:
                self.mejor_individuo = mejor_individuo  # Se actualiza el mejor individuo de la población



# Datos del problema: 10 cajas con sus respectivos precios y pesos
cajas = [
    Caja(1, 100, 300),
    Caja(2, 50, 200),
    Caja(3, 115, 450),
    Caja(4, 25, 145),
    Caja(5, 200, 664),
    Caja(6, 30, 90),
    Caja(7, 40, 150),
    Caja(8, 100, 355),
    Caja(9, 100, 401),
    Caja(10, 100, 395)
]
peso_maximo = 1000  # Peso máximo que la grúa puede cargar
tam_poblacion = 10  # Tamaño de la población
generaciones = 100  # Número de generaciones

# Ejecutar el algoritmo genético
poblacion = Poblacion(cajas, peso_maximo, tam_poblacion)
poblacion.evolucionar(generaciones)  # Evolución de la población
mejor = poblacion.mejor_individuo
print(f"\nMejor individuo: Genotipo = {mejor.genotipo}, Precio = {mejor.precio_total}, Peso = {mejor.peso_total}")
