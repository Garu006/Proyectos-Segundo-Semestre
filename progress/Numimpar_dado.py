'''Pide al usuario un numero y muestra todo los numeros impares hasta ese numero'''

num1 = int(input("Ingresa un numero: "))

for i in range(1, num1 + 1,2):
    print(i)