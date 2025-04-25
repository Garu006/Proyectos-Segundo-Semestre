'''Crea un sistema para gestionar estudiantes y calcular su promedio'''

class Estudiantes:
    def __init__(self, nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas

    def calcular_promedio(self):
        if not self.notas:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f'{self.nombre} {self.apellido} tiene {self.edad} años y {self.notas}'                              