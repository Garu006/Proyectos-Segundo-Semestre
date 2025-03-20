import random

num_secret = random.randint(1,100)
adivina = int(input("Adivina el numero del (1 - 100): "))

if adivina == num_secret:
    print("Correcto!")
else:
    print("Numero equivocado, el numero era: ", num_secret)    