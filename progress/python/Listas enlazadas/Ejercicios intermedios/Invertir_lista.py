'''Crea una funcion que invierta el orden de los nodos de la lista'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
class Lista_Enlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def invertir(self):
        anterior = None
        actual = self.inicio
        while actual:
            siguiente = actual.siguiente
            actual.siguinte = anterior
            anterior = actual
            actual = siguiente
        self.inicio = anterior
        print("La lista fue invertida")

    def mostrar(self):
        actual = self.inicio
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista: ", elementos)

def menu():
    lista = Lista_Enlazada()
    while True:
        print("----------MENU----------")
        print("1.Insertar")
        print("2.Invertir lista")
        print("3.Mostrar lista")
        print("4.Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            valor = int(input("Ingrese un valor: "))
            lista.insertar(valor)
            print("Valor ingresado exitosamente")
        elif opcion == '2':
            lista.invertir()
            print("La lista fue invertida")
        elif opcion == '3':
            lista.mostrar()
        elif opcion == '4':
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()
        