# prompt: Generate an xy point so that -1>x>1 and -1>y>1. If the point is within a radius=1 circle, leave it and print it. Try again otherwise

import random
import math

def point():
    while True: #Generación de los puntos aleatorios
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        if x*x + y*y < 1: #Condiciones dadas en el problema para imprimir los puntos correctos
            return x, y

def main():
    n = 20  # puntos a generar

    for _ in range(n): #Crea un bucle, aqui no necesitamos un valor, por eso el _
        x, y = point() # Genera el punto
        print(f"({x:.5f}, {y:.5f})") #Imprime el punto

if __name__ == "__main__":
    main()
