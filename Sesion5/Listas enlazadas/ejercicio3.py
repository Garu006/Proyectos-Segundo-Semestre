'''Construir un metodo "ImprimeInverso" que imprima los elementos de una lista enlazada de enteros en orden inverso a partir de una posicion "P"'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def ImprimeInverso(self, P):
        elementos = []
        actual = self.cabeza
        contador = 0
        
        # Recorrer la lista y almacenar elementos desde la posición P
        while actual:
            if contador >= P:
                elementos.append(actual.dato)
            actual = actual.siguiente
            contador += 1

        # Imprimir elementos en orden inverso
        if elementos:
            print("Lista inversa desde la posición", P, ":", elementos[::-1])
        else:
            print(f"La posición {P} está fuera de los límites de la lista.")

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
        print("\nMenú de opciones:")
        print("1. Agregar un número a la lista")
        print("2. Imprimir la lista enlazada")
        print("3. Imprimir lista inversa desde una posición P")
        print("4. Salir del programa")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                dato = int(input("Ingrese un número entero: ").strip())
                lista.agregar(dato)
                print(f"Número {dato} agregado a la lista.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        elif opcion == "2":
            lista.mostrar_lista()
        elif opcion == "3":
            try:
                P = int(input("Ingrese la posición desde donde imprimir inverso: ").strip())
                lista.ImprimeInverso(P)
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == '__main__':
    main()
