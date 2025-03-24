'''Imprime un triangulo con asteriscos
basado en el numero de filas que ingrese el usuario'''

fila = int(input("Ingrese el numero de filas para el triangulo: "))

for i in range(1, fila + 1):
    print('*' * i)