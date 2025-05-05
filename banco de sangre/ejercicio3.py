'''En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se almacenan en una pila según el orden en que se procesan.
Si ocurre un problema técnico, se debe revertir el último registro. 
Implementa un sistema para registrar donantes (push), eliminar el último (pop), y mostrar el donante actual en proceso.'''

class PilaDonantes:
    def __init__(self):
        self.donantes = []

    def esta_vacía(self):
        return self.donantes == []

    def push(self, donante):
        self.donantes.append(donante)

    def pop(self):
        if not self.esta_vacía():
            eliminado = self.donantes.pop()
            print(f"Registro eliminado: {eliminado}")
        else:
            print("No hay registros de donantes")

    def mostrar_actual(self):
        if not self.esta_vacía():
            return self.donantes[-1]
        else:
            return "No hay registros de donantes"

def main():
    pila = PilaDonantes()

    while True:
        print("---Donación de sangre---")
        print("1. Registrar donante")
        print("2. Eliminar último registro")
        print("3. Mostrar donante actual")
        print("4. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            nombre = input("Seleccione el nombre del donante: ")
            pila.push(nombre)
            print("Donante registrado")
        elif opcion == 2:
            pila.pop()
        elif opcion == 3:
            actual = pila.mostrar_actual()
            print(f"El donante actual es: {actual}")
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()