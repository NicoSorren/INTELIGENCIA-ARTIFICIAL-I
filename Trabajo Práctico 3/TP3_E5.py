import random
import math

# Clase que representa el tablero del Ta-te-ti
class Board:
    def __init__(self):
        # Inicializa el tablero con espacios vacíos
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        # Imprime el tablero de forma legible
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]}")
            if i < 2:
                print("---------")

    def make_move(self, position, player):
        # Realiza un movimiento si la posición está vacía
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        # Condiciones de victoria para el Ta-te-ti
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        # Verifica si el tablero está lleno y es un empate
        if ' ' not in self.board:
            return 'Tie'
        return None

    def get_empty_positions(self):
        # Devuelve una lista de posiciones vacías en el tablero
        return [i for i, x in enumerate(self.board) if x == ' ']

# Clase que implementa el algoritmo de Recocido Simulado
class SimulatedAnnealing:
    def __init__(self, temperature, cooling_rate):
        self.temperature = temperature
        self.cooling_rate = cooling_rate

    def objective_function(self, board):
        # Función objetivo que evalúa el tablero
        winner = board.check_winner()
        if winner == 'X':
            return 1  # X gana
        elif winner == 'O':
            return -1  # O gana
        return 0  # Empate o tablero incompleto

    def random_move(self, board):
        # Realiza un movimiento aleatorio en una posición vacía
        empty_positions = board.get_empty_positions()
        return random.choice(empty_positions) if empty_positions else None

    def anneal(self, board, player):
        # Inicializa el mejor tablero y su puntuación
        best_board = Board()
        best_board.board = board.board[:]
        best_score = self.objective_function(board)

        # Proceso de enfriamiento
        while self.temperature > 0.1:
            new_board = Board()
            new_board.board = board.board[:]
            move = self.random_move(board)
            if move is not None:
                new_board.make_move(move, player)
                new_score = self.objective_function(new_board)

                # Decide si aceptar el nuevo tablero basado en la función objetivo y la temperatura
                if new_score > best_score or random.random() < math.exp((new_score - best_score) / self.temperature):
                    best_board = new_board
                    best_score = new_score

            # Reduce la temperatura
            self.temperature *= self.cooling_rate

        return best_board

# Clase que maneja el flujo del juego
class Game:
    def __init__(self, initial_temperature=1000, cooling_rate=0.95):
        self.board = Board()
        self.sa = SimulatedAnnealing(initial_temperature, cooling_rate)

    def play(self):
        current_player = 'O'  # El jugador humano comienza como 'O'
        while self.board.check_winner() is None:
            self.board.print_board()
            if current_player == 'O':
                # Movimiento del jugador humano
                move = int(input("Enter your move (0-8): "))
                if self.board.make_move(move, 'O'):
                    current_player = 'X'
            else:
                # Movimiento del algoritmo de Recocido Simulado
                self.board = self.sa.anneal(self.board, 'X')
                current_player = 'O'

        self.board.print_board()
        result = self.board.check_winner()
        if result == 'Tie':
            print("It's a tie!")
        else:
            print(f"{result} wins!")

# Ejecución del juego
if __name__ == "__main__":
    game = Game()
    game.play()
