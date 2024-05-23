# Creación de la clase
class Robot:
  # Inicialización con una cuadrícula, guarda la cuadrícula, las filas, las columnas, y las celdas ya visitadas
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
  # Verifica si un movimiento es válido
    def is_valid_move(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != 1

  # busqueda en profundidad, verifica si una celda ya está visitada, visita la celda, y regresa un true si se llega a la otra esquina
  # de otra forma, busca un movimiento hacia la derecha o hacia abajo válido, y retorna false si no hay movimientos
    def dfs(self, r, c, path):
        if not self.is_valid_move(r, c) or (r, c) in self.visited:
            return False
        
        self.visited.add((r, c))
        if r == self.rows - 1 and c == self.cols - 1:
            return True
        
        if self.dfs(r + 1, c, path) or self.dfs(r, c + 1, path):
            path.append((r, c))
            return True
        
        return False
  # Inicia el dfs y busca el camino, regresa none si no hay un camino posible
    def find_path(self):
        path = []
        if self.dfs(0, 0, path):
            path.append((self.rows - 1, self.cols - 1))
            path.reverse()
            return path
        else:
            return None

# Ejemplo de uso:
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

robot = Robot(grid)
path = robot.find_path()

if path:
    print("Ruta encontrada:")
    for r, c in path:
        print(f"({r}, {c})")
else:
    print("No se encontró una ruta válida.")
