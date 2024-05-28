from collections import deque

def pour(jug1, jug2):
    max1, max2 = 5, 3  # Capacidad de ambas jarras
    visited = set()    # Almacena los 'estados' ya visitados
    queue = deque([(0, 0)])  # Estado inicial de las jarras

    while queue:
        current = queue.popleft()
        print("Estado Actual:", current)
        if current[0] == 4 or current[1] == 4:  # Checa si la condición de los 4 litros de ha cumplido
            return current
        visited.add(current)

        # Define los posibles movimientos (Vaciar de una jarra a otra, llenar o vaciar una jarra)
        moves = [(max(current[0] - (max2 - current[1]), 0), min(current[0] + current[1], max2)),
                 (min(current[0] + current[1], max1), max(current[1] - (max1 - current[0]), 0)),
                 (max(current[0] - max2 + current[1], 0), 0),
                 (0, max(current[1] - max1 + current[0], 0)),
                 (max1, current[1]),
                 (current[0], max2)]
        
        # Añade los movimientos validos a la cola
        for move in moves:
            if move not in visited:
                queue.append(move)
                visited.add(move)

result = pour(0, 0)
print("Final:", result)
