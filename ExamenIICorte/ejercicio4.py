''': Implementación de una cola de prioridad. Diseñe una cola de prioridad
donde los elementos se desencolan según su prioridad. Cada elemento tendrá un
nombre y una prioridad (un número entero, donde un número menor indica mayor
prioridad).'''

class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad {self.prioridad})"

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, nombre, prioridad):
        nuevo = Elemento(nombre, prioridad)
        insertado = False
        for i in range(len(self.cola)):
            if prioridad < self.cola[i].prioridad:
                self.cola.insert(i, nuevo)
                insertado = True
                break
        if not insertado:
            self.cola.append(nuevo)

    def desencolar(self):
        if not self.esta_vacia():
            elemento = self.cola.pop(0)
            print(f"Atendiendo: {elemento}")
        else:
            print("La cola está vacía.")

    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print("Cola de prioridad:")
            for i, elemento in enumerate(self.cola):
                print(f"{i+1}. {elemento}")

    def esta_vacia(self):
        return len(self.cola) == 0

# Función principal
def main():
    cola = ColaPrioridad()
    while True:
        print("\n--- Menú Cola de Prioridad ---")
        print("1. Agregar elemento")
        print("2. Atender elemento con mayor prioridad")
        print("3. Mostrar cola actual")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del elemento: ")
            prioridad = int(input("Prioridad (menor número = mayor prioridad): "))
            cola.encolar(nombre, prioridad)
            print("Elemento agregado.")
        elif opcion == '2':
            cola.desencolar()
        elif opcion == '3':
            cola.mostrar()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
