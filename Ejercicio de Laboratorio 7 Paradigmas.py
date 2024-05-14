import math
import random

class Punto3D:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
    
    # Métodos set
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
    
    def set_z(self, z):
        self.__z = z
    
    # Métodos get
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    
    def distancia(self, otro_punto):
        dx = self.__x - otro_punto.get_x()
        dy = self.__y - otro_punto.get_y()
        dz = self.__z - otro_punto.get_z()
        distancia_euclidiana = math.sqrt(dx**2 + dy**2 + dz**2)
        return distancia_euclidiana

# Crear arreglo de 10 objetos Punto3D con coordenadas aleatorias
puntos = [Punto3D(random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)) for _ in range(10)]

# Calcular distancias entre todos los puntos y determinar la menor distancia
menor_distancia = float('inf')  # Inicializar con un valor infinito
punto_a = None
punto_b = None

for i in range(len(puntos)):
    for j in range(i+1, len(puntos)):
        distancia_actual = puntos[i].distancia(puntos[j])
        if distancia_actual < menor_distancia:
            menor_distancia = distancia_actual
            punto_a = puntos[i]
            punto_b = puntos[j]

print("La menor distancia es:", menor_distancia)
print("Entre los puntos:", punto_a.get_x(), punto_a.get_y(), punto_a.get_z(), "y", punto_b.get_x(), punto_b.get_y(), punto_b.get_z())
