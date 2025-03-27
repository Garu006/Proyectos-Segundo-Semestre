'''Elabore un programa para calcular la quinta potencia, la raiz cuadrada
el exponencial, el logaritmo natural y el valor absoluto de un numero introducido
por el teclado'''

import math
num1 = float(input("Ingresa un numero: "))

print("El resultado de la quinta potencia es: ", num1 ** 5)
print("El resultado de la raiz cuadrada es: ", math.sqrt(num1))
print("El resultado de la exponencial es: ", math.exp(num1))
print("El resultado de el logaritmo natural es: ", math.log(num1))
print("El resultado del valor absoluto es:", abs(num1))