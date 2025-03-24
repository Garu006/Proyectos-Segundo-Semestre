'''Genera la tabla de multiplicar de un numero usando while'''

num1 = int(input("Ingresa un numero: "))

i = 1

while i <= 10:
    print(f"{num1} x {i} = {num1 * i}")
    i += 1