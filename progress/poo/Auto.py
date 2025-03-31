class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El auto ha acelerado. Velocidad actual: {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"El auto ha frenado. Velocidad actual: {self.velocidad} km/h")

# Prueba de la clase
auto1 = Auto("Toyota", "Corolla")
auto1.acelerar(30)
auto1.acelerar(20)
auto1.frenar(10)
auto1.frenar(50)
