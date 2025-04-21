'''Implementar un metodo que recibe una lista de enteros 'L' y un numero entero 'n' de forma que modifique la lista mediante el borrado de todos los elementos de la lista que tengan este valor'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    

class lista_enlazada:
    def __init__(self):
        self.inicio = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.inicio
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista: ", elementos)


    def eliminar_valor(self, valor):
        while self.inicio and self.inicio.valor == valor:
            self.inicio = self.inicio.siguiente

        actual = self.inicio
        anterior = None

        while actual:
            if actual.valor == valor:
                anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

if __name__ == "__main__":
    lista = lista_enlazada()
    
    while True:
        print("-----Menu de lista enlazada-----")
        print("1. Agregar elemento")
        print("2. Mostrar lista")
        print("3. Eliminar elemento")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == '1':
            dato = int(input("Ingresa un numero: "))
            lista.agregar(dato)
            print("Elemento agregado con exito")
        elif opcion == '2':
            lista.mostrar()
        elif opcion == '3':
            valor = int(input("Ingresa el numero que quieres eliminar: "))
            lista.eliminar_valor(valor)
            print("Elemento eliminado con exito")
        elif opcion == '4':
            print("Saliendo del prograa")
            break
        else:
            print("Opcion invalida, Intentelo de nuevo") 