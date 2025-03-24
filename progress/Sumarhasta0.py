'''Suma los numeros que el usuario ingrese hasta que ingrese un 0 para
 finalizar'''

suma = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)