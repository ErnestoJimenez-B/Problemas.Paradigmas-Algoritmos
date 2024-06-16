import random

def point():
    x = 2 * random.random() - 1 # parecido al codigo anterior, genera puntos 
    y = 2 * random.random() - 1 # aleatorios 
    return x, y                 

def main():
    n = 100000000  # Generación de los puntos
    inside_circle = 0  # Contador para los puntos dentro del círculo

    for _ in range(n): # loop
        x, y = point() # Genera el punto
        if x*x + y*y < 1: # checa la condición
            inside_circle += 1 # suma 1 a inside_circle si se cumple

    # Calculo del valor aproximado de pi
    pi_approx = (inside_circle / n) * 4
    print(f"Approximated value of π: {pi_approx}") #Hace el cálculo e imprime

if __name__ == "__main__": # Inicialización
    main()
