'''Pide al usuario ingresar varios numeros y cuenta cuantos son positivos y cuantos son negativos.
El ciclo termina cuando el usuario ingrese un 0'''

positivo = 0
negativo = 0

while True:
    num = int(input("Ingresa un numero (0 para terminar)"))
    if num == 0:
        break
    elif num > 0:
        positivo += 1
    else:
        negativo += 1

print("Numeros positivos: ", positivo)
print("Numeros negativos: ", negativo)
