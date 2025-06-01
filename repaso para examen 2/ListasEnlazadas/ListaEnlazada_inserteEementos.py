'''Crea una clase "ListaEnlazada" que permita agregar elementos al final de la lista.
Luego implementa un metodo para recorrer y mostrar todos los elementos de la lista'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
def main():
    lista = ListaEnlazada()

    while True:
        print("--- Lista ---")
        print("1. Agregar")
        print("2. Recorrer")
        print("3. Salir")
        opcion = int(input("Elige una opcion: "))
        if opcion == 1:
            print("Introduce el dato a agregar: ")
            dato = int(input())
            lista.agregar(dato)
            print("agregado")
        elif opcion == 2:
            lista.recorrer()
        elif opcion == 3:
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentelo nuevamente")

if __name__ == "__main__":
    main()