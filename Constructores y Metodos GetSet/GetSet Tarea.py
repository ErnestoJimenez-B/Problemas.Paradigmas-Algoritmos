class Persona:
    def __init__(self, nombre, veces, edad, direccion, nombre_madre, nombre_padre, escuela):
        self.nombre = nombre
        self.veces = 1
        self.edad = edad
        self.direccion = direccion
        self.nombre_madre = nombre_madre
        self.nombre_padre = nombre_padre
        self.escuela = escuela

    def saludar(self):
        for i in range(self.veces):
            print(f'Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.direccion}, mis padres son {self.nombre_madre} y {self.nombre_padre}, y voy a la escuela {self.escuela}')

    def __str__(self):
        return f'Nombre: {self.nombre}, veces: {self.veces}, edad: {self.edad}, dirección: {self.direccion}, nombre madre: {self.nombre_madre}, nombre padre: {self.nombre_padre}, escuela: {self.escuela}'

persona1 = Persona('AGF', 2, 25, 'Calle 123', 'Maria', 'Juan', 'Escuela XYZ')
persona1.saludar()
print(persona1)
