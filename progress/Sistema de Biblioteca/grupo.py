'''Crea un sistema para gestionar estudiantes y calcular su promedio'''

from estudiantes import Estudiantes 

class Grupo:
    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiantes(self, estudiantes: Estudiantes):
            self.estudiantes.append(estudiantes)
    
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes en este grupo")
        else:
            for est in self.estudiantes:
                print(est)

    