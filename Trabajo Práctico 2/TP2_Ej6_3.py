class Estado:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
       
class Problema:
    def __init__(self, estado_inicial, estado_objetivo, acciones, costos):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acciones = acciones
        self.costos = costos            ##Agrego el diccionario de costos que mapea la acción y el costo de llevarla a cabo

def a_estrella(estado, problema, explorados, costo_acumulado):
    explorados.add(estado)
    if estado == problema.estado_objetivo:
        return [estado]
    
    # Ordena las acciones disponibles por la combinación de heurística y costo acumulado
    acciones_ordenadas = sorted(problema.acciones[estado.nombre].items(), key=lambda x: problema.heuristicas[x[1].nombre] + problema.costos[estado.nombre][x[0]])
    
    for accion, nuevo_estado in acciones_ordenadas:
        if nuevo_estado not in explorados:
            nuevo_costo_acumulado = costo_acumulado + problema.costos[estado.nombre][accion]
            solucion = a_estrella(nuevo_estado, problema, explorados, nuevo_costo_acumulado)
            if solucion:
                return [estado] + solucion
    return None


if __name__ == '__main__':
    
    accUp = Accion('arriba')
    accDown = Accion('abajo')
    accL = Accion('izquierda')
    accR = Accion('derecha')

    i = Estado('I', [accDown, accL, accR])
    g = Estado('G', [accR, accDown])
    q = Estado('Q', [accUp, accL, accR])
    w = Estado('W', [accL, accR])
    p = Estado('P', [accUp, accR])
    r = Estado('R', [accL,  accR])
    t = Estado('T', [accUp, accL])
    k = Estado('K', [accUp, accR, accDown, accL])
    c = Estado('C', [accUp, accDown])
    m = Estado('M', [accUp, accDown, accL, accR])
    f = Estado('F', [accUp])
    a = Estado('A', [accR, accDown])
    d = Estado('D', [accUp, accDown])
    b = Estado('B', [accL, accDown])
    n = Estado('N', [accUp, accL])
    e = Estado('E', [accDown])
    
    estado_inicial = i
    estado_objetivo = f
    acciones = {'I':{'abajo': q,
                     'izquierda': g,                    
                    'derecha': w},
                'G':{'derecha': i,
                     'abajo': p},
                'Q':{'arriba': i,
                     'izquierda': p,
                     'derecha': r},
                'W':{'izquierda': i,
                     'derecha': k},
                'P':{'arriba': g,
                     'derecha': q},
                'R':{'izquierda': q,
                     'derecha': t}, 
                'T':{'arriba': k,
                     'izquierda': r},
                'K':{'arriba': c,
                     'derecha': m,
                     'abajo': t,
                    'izquierda': w},
                'C':{'arriba': a,
                     'abajo': k},
                'M':{'arriba': d,
                    'abajo': f,
                    'izquierda': k,
                    'derecha': n},
                'F':{'arriba': m},
                'A':{'derecha': b,
                     'abajo': c},
                'D':{'arriba': b,
                     'abajo': m},
                'B':{'izquierda': a,
                    'abajo': d},
                'N':{'arriba': e,
                     'izquierda': m}, 
                'E':{'abajo': n},                                                                                                                                      
                     }
    
    costos = {'I':{'abajo': 1,
                   'izquierda': 1,
                    'derecha': 31},
                'G':{'derecha': 1,
                     'abajo': 1},
                'Q':{'arriba': 1,
                     'izquierda': 1,
                     'derecha': 1},
                'W':{'izquierda': 1,
                     'derecha': 1},
                'P':{'arriba': 1,
                     'derecha': 1},
                'R':{'izquierda': 1,
                     'derecha': 1}, 
                'T':{'arriba': 1,
                     'izquierda': 1},
                'K':{'arriba': 1,
                     'derecha': 1,
                     'abajo': 1,
                    'izquierda': 31},
                'C':{'arriba': 1,
                     'abajo': 1},
                'M':{'arriba': 1,
                    'abajo': 1,
                    'izquierda': 1,
                    'derecha': 1},
                'F':{'arriba': 1},
                'A':{'derecha': 1,
                     'abajo': 1},
                'D':{'arriba': 1,
                     'abajo': 1},
                'B':{'izquierda': 1,
                    'abajo': 1},
                'N':{'arriba': 1,
                     'izquierda': 1}, 
                'E':{'abajo': 1},                                                                                                                                      
                     }

    
    heuristicas = {
            'I': 4, 'G': 6, 'P': 8, 'Q': 8, 'R': 8, 'T': 8,
            'W': 4, 'K': 4, 'M': 4, 'N': 6, 'E': 8, 'F': 0,
            'C': 6, 'A': 8, 'B': 8, 'D': 8
        }
    
    problema = Problema(estado_inicial, estado_objetivo, acciones, costos)
    problema.heuristicas = heuristicas  # Agrega el diccionario de heuristicas al problema
    
    explorados = set()
    solucion = a_estrella(estado_inicial, problema, explorados, 0) ##El cero implica el costo acumulado desde el estado inicial es nulo

if solucion:
    print("Camino encontrado:")
    costo_total = 0  # Inicializa el costo total del camino
    for estado in solucion:
        if estado.nombre != estado_inicial.nombre: ##Encuentra la acción previa (en función del estado anterior y el actual)
            accion_previa = next(accion for accion, siguiente_estado in problema.acciones[estado_anterior.nombre].items() if siguiente_estado == estado)
            costo_total += problema.costos[estado_anterior.nombre][accion_previa]    ##Suma el costo de la acción previa al costo total del camino
        estado_anterior = estado
        camino = " ".join([estado.nombre for estado in solucion])
    print(camino)
else:
    print("No hay solución")