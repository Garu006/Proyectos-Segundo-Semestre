'''Crea un sistema para gestionar estudiantes y calcular su promedio'''

from grupo import Grupo
from estudiantes import Estudiantes

def main():
    nombre_grupo = input("Ingrese el nombre del grupo: ")
    grupo = Grupo(nombre_grupo, [])

    while True:
        print("--------- MENU ---------")
        print("1. Agregar estudiantes")
        print("2. Mostrar estudiantes")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            notas = input("Ingrese las notas del estudiante (separadas por comas): ")
            notas = notas.split(",")
            notas = [int(nota) for nota in notas]
            estudiante = Estudiantes(nombre, apellido, edad, notas)
            grupo.agregar_estudiantes(estudiante)
            print("Estudiante agregado")
        elif opcion == "2":
            grupo.mostrar_estudiantes()
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opcion ingresada incorrecta, intente nuevamente")

if __name__ == "__main__":
    main()