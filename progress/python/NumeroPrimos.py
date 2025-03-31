'''Verifica si un numero ingresado es primo o no'''
num1 = int(input("Ingresa un numero: "))
num_primo = True

if num1 < 2:
    num_primo = False
else:
    for i in range(2, num1):
        if num1 % i == 0:
            num_primo = False
            break

if num_primo:
    print("Es un numero primo")
else:
    print("No es un numero primo")

