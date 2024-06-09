# Definición de la función que cuenta los caminos
def count_paths(maze):
    # Obtener las dimensiones del laberinto
    m = len(maze)  # Número de filas
    n = len(maze[0])  # Número de columnas

    # Crear una matriz de soluciones dp con las mismas dimensiones que el laberinto
    dp = [[0] * n for _ in range(m)]  # Inicializa una matriz llena de ceros

    # Inicializar la celda de inicio
    if maze[0][0] == 0:  # Si la celda de inicio no es un obstáculo
        dp[0][0] = 1  # Hay un camino posible

    # Llenar la primera fila
    for j in range(1, n):
        if maze[0][j] == 0:  # Si la celda actual no es un obstáculo
            dp[0][j] = dp[0][j-1]  # Copiar el valor de la celda anterior

    # Llenar la primera columna
    for i in range(1, m):
        if maze[i][0] == 0:  # Si la celda actual no es un obstáculo
            dp[i][0] = dp[i-1][0]  # Copiar el valor de la celda superior

    # Llenar el resto de la matriz dp
    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] == 0:  # Si la celda actual no es un obstáculo
                # Sumar los caminos posibles de las celdas superiores e izquierdas
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # El resultado será el valor en la celda dp[m-1][n-1], que representa la esquina inferior derecha
    return dp[m-1][n-1]

# Ejemplo de uso
maze = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(count_paths(maze))
