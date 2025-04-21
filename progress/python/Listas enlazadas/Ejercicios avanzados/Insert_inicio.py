'''Crea un metodo que inserte un nuevo nodo al principio de la lista'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def eliminar_valor(self, valor):
        actual = self.inicio
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                print(f"Elemento {valor} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"Elemento {valor} no encontrado.")

    def mostrar(self):
        actual = self.inicio
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista:", elementos)

def menu():
    lista = ListaEnlazada()

    while True:
        print("\n--- MENÚ DE LISTA ENLAZADA ---")
        print("1. Insertar al inicio")
        print("2. Eliminar un valor")
        print("3. Mostrar lista")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            valor = int(input("Ingresa el valor a insertar: "))
            lista.insertar_al_inicio(valor)
        elif opcion == '2':
            valor = int(input("Ingresa el valor a eliminar: "))
            lista.eliminar_valor(valor)
        elif opcion == '3':
            lista.mostrar()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
