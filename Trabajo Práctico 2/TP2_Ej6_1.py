##Búsqueda primero en profundidad
##Definiciones de clases

class Estado:                                   ##Para representar un estado en el problema, dando el nombre y la lista
    def __init__(self, nombre, acciones):       ##acciones para dicho estado
        self.nombre = nombre
        self.acciones = acciones

class Accion:                                   ##Para representar los movimientos que se pueden hacer
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
       
class Problema:                                 ## Es el problema a resolver
    def __init__(self, estado_inicial, estado_objetivo, acciones):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acciones = acciones

def profundidad(estado, problema, explorados):  ##Función de búsqueda
    explorados.add(estado)                      ##Marca el estado actual como explorado
    if estado == problema.estado_objetivo:
        return [estado]                         ## Devolver la lista en caso de alcanzar el objetivo
    for accion, nuevo_estado in problema.acciones[estado.nombre].items(): ##Explora las acciones posibles desde el estado actual
        if nuevo_estado not in explorados:
            solucion = profundidad(nuevo_estado, problema, explorados)  ##Verifica si el nuevo estado no ha sido explorado 
            if solucion:
                return [estado] + solucion          ##Agrega el estado actual y la solución encontrada
    return None

##Definiciones
if __name__ == '__main__':
    ##Defino los movimientos
    accUp = Accion('arriba')
    accDown = Accion('abajo')
    accL = Accion('izquierda')
    accR = Accion('derecha')
    ##Defino cada uno de los estados y le asigno el nombre y la acción que pueden llevar a cabo 
    i = Estado('I', [accL, accDown, accR])
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
    ##Defino las acciones que se llevan a cabo a partir de cada estado, y a qué estado se alcanza con cada paso
    ## Importa el orden, está hecho de forma tal que recorra el árbol como nosotros lo diseñamos (por orden los nodos en un mismo nivel están
    ## ordenados alfabéticamente)
    acciones = {'I':{'izquierda': g,
                     'abajo': q,
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
    
    problema = Problema(estado_inicial, estado_objetivo, acciones) ##Instancia de la clase problema, que luego es accedida por "solucion"
    explorados = set() ##Conjunto que almacena los distintos estados ya explorados
    solucion = profundidad(estado_inicial, problema, explorados)   ##Llama a la función de búsqueda
    ##Mostrar la solución
    if solucion:
        print("Camino encontrado:")
        for estado in solucion:
            camino = " ".join([estado.nombre for estado in solucion])
        print(camino)

    else:
        print("No hay solución")
