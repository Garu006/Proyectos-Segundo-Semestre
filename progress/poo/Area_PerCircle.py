'''Crea una clase "circulo" que tenga un radio y metodos para calcular su area y perimetro'''

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pu * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
#Prueba de la clase
c1= Circulo(5)
print(f"Area: {c1.area():.2f}")
print(f"Perimetro: {c1.perimetro():.2f}")