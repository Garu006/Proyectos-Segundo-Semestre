class CuentaBancaria:
    def __init__(self,titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, cantidad):
        self.saldo += cantidad
        print(f"Su deposito es de {cantidad}. Nuevo saldo: ${self.saldo}")
    
    def retiro(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad
            print(f"Retido de ${cantidad}. Nuevo saldo: ${self.saldo}")

#Prueba de la clase
cuenta1 = CuentaBancaria("Gabriel", 10)
cuenta1.deposito(10)
cuenta1.retiro(15)
cuenta1.retiro(6) #Intento de retiro sin fondos insuficientes