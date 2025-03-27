"""Calcular la nota de n estudiantes para los tres cortes de evaluacion 
de asignatura algoritmos y estructuras de datos"""

print("\n Nota final de asignatura")
n = int(input("Ingresa la cantidad de estudiantes a evaluar: "))

contador = 0

while contador < n:
    print("Ingresa el nombre del estudiante", contador+1, ":", end=' ')
    nombre = input()
    print("Ingresa el la primer nota del estudiante: ", contador+1, ":", end=' ')
    nota1 = float(input())
    print("Ingresa el la segunda nota del estudiante: ", contador+1, ":", end=' ')
    nota2 = float(input())
    print("Ingresa el la tercera nota del estudiante: ", contador+1, ":", end=' ')
    nota3 = float(input())

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio < 69:
        print("\nReprobado")
    elif(promedio >= 70 and promedio <= 79):
        print("\nRegular")
    elif(promedio >= 80 and promedio <=89):
        print("\nBueno")
    elif(promedio >= 90 and promedio <= 100):
        print("\nExcelente") 
        
    contador += 1

print("\n\n")