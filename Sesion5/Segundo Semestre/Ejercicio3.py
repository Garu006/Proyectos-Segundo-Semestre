'''Construir un metodo "ImprimeInverso" que recibba los elementos de una lista enlazada de enteros en orden inverso a partir de una posicion P'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None #Primer nodo de la lista

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def ImprimmirInverso(self, P):
        elementos = []
        actual = self.cabeza
        contador = 0

        #Recorrer la lista y almacenar elementos desde la posicion P
        while actual:
            if contador >= P:
                elementos.append(actual.dato)
            actual = actual.siguiente
            contador += 1

        #Imprimir elementos en orden inverso
        if elemntos:
            print("Lista inversa desde la posicion", P, ":", elementos[::-1])
        else:
            print(f"La posicion {P} esta afuera de los elementos de la lista")

    def mostrar_lista(self):
        actual = self.cabeza
        if actual is None:
            print("Elementos de la lista enlazada: ")
            while actual:
                print(f"-> {actual.dato}")
                actual = actual.siguiente

def main():
    lista = ListaEnlazada()
    
    while True:
        print("\nMenu de opciones: ")
        print("1. Agregar un numero a la lista")
        print("2. Imprimir la lista enlazada")
        print("3. Imprimir lista inversa desde una posicion P")
        print("4. Salir del programa")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            try:
                dato = int(input("Ingrese un numero entero:").strip())
                lista.agregar(dato)
                print(f"Numero {dato} agregado a la lista")
            except ValueError:
                print("Error. Debe ingresar un numero entero")
        elif opcion == "2":
            lista.mostrar_lista()
        elif opcion == "3":
            try:
                P = int(input("Ingrese la posicion desde donde imprimir inverso: ").strip())
                lista.ImprimirInverso(P)
            except ValueError:
                print("Error: Debe ingresar un numero entero valido")
        elif opcion == "4":
            print("Saliendod del programa")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo")

if __name__ == "__main__":
    main()