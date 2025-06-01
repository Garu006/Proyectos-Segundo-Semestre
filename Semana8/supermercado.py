'''Simulación de Supermercado'''
#Definimos la clase Supermercado
class Supermercado:
    #Constructor de la clase
    def __init__(self):
        #Inicializamos la lista vacia que contendra los clientes
        self.cliente = []
    #metodo para registrar un cliente en la cola
    def registrar(self, nombre):
        #Agregamos el nombre del cliente al final de la lista
        self.cliente.append(nombre)
    #Metodo para antender al siguiente cliente en la cola
    def atender(self):
        #Verificamos si hay clientes en la cola
        if self.cliente:
            #Removemos el primer cliente de la lista (el que llego primero) y lo mostramos
            atendido = self.cliente.pop(0)
            print(f"El cliente {atendido} ha sido atendido")
        else:
            print("No hay clientes en espera")
    #Metodo para imprimir la lista de clientes en espera
    def imprimir(self):
        if self.cliente:
            print("Lista de clientes en espera de atender: ")
            for i, cliente in enumerate(self.cliente, start=1):
                print(f"{i}. {self.cliente}")
        else:
            print("No hay datos en la cola")
#Funcion que muestra el menu y permite interactuar con la cola
def menu():
    #Instancia de la clase Supermercado
    supermercado = Supermercado()
    #Bucle infinito para el menu (se detiene cuando el usuario seleccione la opcion de salir)
    while True:
        #Menu de opciones
        print("Programa de atencion al cliente")
        print("1. Registrar cliente")
        print("2. Atender cliente")
        print("3. Imprimir lista de clientes")
        print("4. Salir")
        #Solicitamos la opcion al usuario
        opcion = int(input("Seleccione una opcion: "))
        #Registramos el cliente
        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            supermercado.registrar(nombre)
        #Atendemos al cliente en la cola si existe 
        elif opcion == 2:
            supermercado.atender()
        #Imrimimos la lista de clientes en espera
        elif opcion == 3:
            supermercado.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentelo nuevamente")
#Punto de entrada del programa
if __name__ == "__main__":
    menu()



    
