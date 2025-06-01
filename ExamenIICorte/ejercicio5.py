'''Búsqueda en una lista enlazada. Cree una función que busque un valor
específico en una lista enlazada. La función debe devolver la posición del valor si se
encuentra, o un mensaje indicando que el valor no está en la lista.'''

class Nodo: 
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None  # No es necesario si no se usa

    def __str__(self):
        return f"{self.valor}"

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            print("Lista enlazada: ")
            while actual:
                print(f"{actual.valor}", end=" ")
                actual = actual.siguiente
            print()

    def buscar(self, valor):
        actual = self.cabeza
        i = 0
        while actual:
            if actual.valor == valor:
                return i
            actual = actual.siguiente
            i += 1
        return "Valor no encontrado"

def main():
    lista = ListaEnlazada()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar valor")
        print("2. Mostrar lista")
        print("3. Buscar valor")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            valor = input("Ingrese un valor: ")
            lista.agregar(valor)
            print("Valor agregado.")
        elif opcion == 2:
            lista.mostrar()
        elif opcion == 3:
            valor = input("Ingrese el valor a buscar: ")
            posicion = lista.buscar(valor)
            if isinstance(posicion, int):
                print(f"Valor encontrado en la posición {posicion}")
            else:
                print(f"{posicion}")
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
