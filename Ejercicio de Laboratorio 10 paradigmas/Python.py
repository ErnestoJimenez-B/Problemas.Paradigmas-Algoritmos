import math
# clase Figure con atributos para el color, perimetro, y area
# constructor para inicializar el color
class Figure:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def perimeter(self):
        pass

    def area(self):
        pass
# Clase para el triangulo, con sus respectivas formulas para 
# Perimetro y Area y el constructor para el color
class Triangle(Figure):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

# Clase para el CIRCULO
# con sus respectivas formulas para 
# Perimetro y Area y el constructor para el color
class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Clase para el RECTANGULO
# con sus respectivas formulas para 
# Perimetro y Area y el constructor para el color

class Rectangle(Figure):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

# Clase para el HEXAGONO
# con sus respectivas formulas para 
# Perimetro y Area y el constructor para el color

class Hexagon(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return 6 * self.side

    def area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2

# Instancias de clase derivada con los datos como el color y 
# las dimensiones.
# Demostracion de polimorfismo
triangle = Triangle("Rojo", 3, 4, 5)
circle = Circle("Azul", 5)
rectangle = Rectangle("Verde", 4, 6)
hexagon = Hexagon("Amarillo", 4)
# arreglo
figures = [triangle, circle, rectangle, hexagon]
# Ejecución
for figure in figures:
    print("Color:", figure.getColor())
    print("Perímetro:", figure.perimeter())
    print("Área:", figure.area())
    print()
