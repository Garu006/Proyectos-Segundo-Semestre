'''Construir un metodo "cantVocales" que determine la cantidad de vocales almacenadas en una lista de caracteres.'''

class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    def agregar(self, caracter):
        nuevo_nodo = Nodo(caracter)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def cantVocales(self):
        vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        actual = self.cabeza
        contador = 0
        while actual:
            if actual.dato in vocales:
                contador += 1
            actual = actual.siguiente
        return contador

    def mostrar_lista(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía")
        else:
            print("Elementos de la lista enlazada:")
            while actual:
                print(f"-> {actual.dato}")
                actual = actual.siguiente

def main():
    lista = ListaEnlazada()

    while True:
        print("\nMenu de opciones")
        print("1. Agregar un carácter")
        print("2. Contar vocales")
        print("3. Mostrar la lista enlazada")
        print("4. Salir")
        print("Elija su opción:", end=" ")
        opcion = input()

        if opcion == "1":
            caracter = input("Ingrese un carácter: ")
            if len(caracter) == 1:  # Solo permite agregar un carácter
                lista.agregar(caracter)
                print(f"Carácter '{caracter}' agregado")
            else:
                print("Solo se permite un carácter")
        elif opcion == "2":
            print(f"Cantidad de vocales en la lista: {lista.cantVocales()}")
        elif opcion == "3":
            lista.mostrar_lista()
        elif opcion == "4":
            print("Salida del programa")
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")

if __name__ == '__main__':
    main()