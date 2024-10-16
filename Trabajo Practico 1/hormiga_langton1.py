import pygame as pg

class App:                                                          # Método constructor __init__ es un método especial que se llama automáticamente cuando creas una nueva instancia de la clase. 
    def _init_(self, WIDTH=16000, HEIGHT=900, CELL_SIZE=12):        # Resolución de pantalla y tamaño de celda (altura 900 pixeles y ancho 16000 pixeles)
        pg.init()                                                   # Inicializar modulos de pygame
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])          # Crea una ventana de visualización de pygame con las dimensiones especificadas (WIDTH x HEIGHT) y la asigna al atributo screen del objeto
        self.clock = pg.time.Clock()                                # Instancia de clase clock para setear fps

        self.CELL_SIZE = CELL_SIZE
        self.ROWS = HEIGHT // CELL_SIZE                             # Calcula numero de filas
        self.COLS= WIDTH // CELL_SIZE     
        self.grid = [[0 for col in range (self.COLS)] for row in range(self.ROWS)]  # List comprehension.  crea una lista de listas: una lista para cada fila, y cada lista de fila contiene self.COLS elementos que son 0.
                                                                                    # Es decir, es un array de dos dimensiones
    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]    