'''Pide un numero al usuario y determina si es positivo, negativo o cero'''

num1 = float(input("Ingresa un numero: "))

if num1 > 0:
    print("El numero es positivo")
elif num1 < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")