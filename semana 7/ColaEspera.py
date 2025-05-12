class Cola:
    def __init__(self):
        self.lista = []

    def esta_vacia(self):
        return len(self.lista) == 0
    
    def encolar(self, nombre):
        if len(self.lista) != 3: 
            self.lista.append(nombre)
            return True
        else:
            return False   

    def desencolar(self):
        return self.lista.pop()

    def verfrente(self):
        return self.lista[0]

    def imprimir(self):
        return self.lista
    
    def longitud(self):
        return len(self.lista)

def menu():
    cola = Cola()

    while True:
        print("\n-----MENU------")
        print("1. Agregar clientes")
        print("2. Atender clientes")
        print("3. Verificar si cola esta vacia")
        print("4. Ver siguiente cliente a atender")
        print("5. ver lista de clientes en espera")
        print("6. Salir")
        print("-----------------")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            cola.encolar(nombre)
        elif opcion == 2:
            atendido = cola.desencolar()
            if atendido:
                print(f"El cliente {atendido} ha sido antendido.")
            else:
                print("La cola estaa vacia.")
        elif opcion == 3:
            if cola.esta_vacia():
                print("La cola esta vacia.")
            else:
                print("Hay clientes en espera.")
        elif opcion == 4:
            if cola.esta_vacia():
                siguiente = cola.verfrente()
                if siguiente:
                    print(f"El siguiente cliente a ser atendido es: {siguiente}")
                else:
                    print("La cola esta vacia.")
        elif opcion == 5:
            print("Lista de clientes en espera: ", cola.imprimir())
        elif opcion == 6:
            print("Salida del programa.")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()