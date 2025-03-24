'''Muestra los primeros numeros de la serie de fibonacci'''

num1 = int(input("Cuantos numeros de fibonacci quieres: "))

a, b = 0, 1

for _ in range(num1):
    print(a, end=" ")
    a, b = b, a + b