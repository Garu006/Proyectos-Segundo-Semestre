'''Simulación de una lista de reproducción de música. Implemente una
lista de reproducción de música utilizando una lista enlazada. El programa debe permitir
agregar canciones, eliminar canciones, reproducir la siguiente canción, reproducir la
canción anterior y mostrar la lista de reproducción actual.'''

class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

class ListaReproduccion:
    def __init__(self):
        self.actual = None  # Puntero a la canción en reproducción
        self.primera = None

    def agregar_cancion(self, nombre):
        nueva = NodoCancion(nombre)
        if self.primera is None:
            self.primera = nueva
            self.actual = nueva
        else:
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    def eliminar_cancion(self, nombre):
        temp = self.primera
        while temp:
            if temp.nombre == nombre:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior
                print(f"'{nombre}' eliminada de la lista.")
                return
            temp = temp.siguiente
        print(f"'{nombre}' no encontrada en la lista.")

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"🎵 Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay siguiente canción.")

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"🎵 Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay canción anterior.")

    def mostrar_lista(self):
        temp = self.primera
        if not temp:
            print("🎶 Lista de reproducción vacía.")
            return
        print("🎶 Lista de reproducción:")
        while temp:
            actual_marcada = " <- (Reproduciendo)" if temp == self.actual else ""
            print(f"- {temp.nombre}{actual_marcada}")
            temp = temp.siguiente

# Función principal
def main():
    lista = ListaReproduccion()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la canción: ")
            lista.agregar_cancion(nombre)
        elif opcion == '2':
            nombre = input("Nombre de la canción a eliminar: ")
            lista.eliminar_cancion(nombre)
        elif opcion == '3':
            lista.siguiente_cancion()
        elif opcion == '4':
            lista.anterior_cancion()
        elif opcion == '5':
            lista.mostrar_lista()
        elif opcion == '6':
            print("Saliendo del reproductor...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
