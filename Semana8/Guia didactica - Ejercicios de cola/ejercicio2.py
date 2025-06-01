'''Cree un sistema que simule la atención de llamadas en un Call Center.
Cada llamada debe ingresar a una cola con datos commo el nombre del cliente y el motivo de la llamada.
A medida que los agentes estén disponibles, se debe atender al siguiente cliente en orden de llegada.'''

class Cola:
    def __init__(self):
        self.llamadas = []
    
    def agregar(self, nombre, motivo):
        llamada = {
            "nombre": nombre,
            "motivo": motivo,
        }
        self.llamadas.append(llamada)
        print(f"Se ha añadido la llamada {nombre} con motivo {motivo} a la cola")
    
    def atender(self):
        if self.llamadas:
            llamada = self.llamadas.pop(0)
            print(f"Se ha antendido la llamada {llamada['nombre']} con motivo {llamada['motivo']}")
        else:
            print("No hay llamadas en la cola")
    
    def imprimir(self):
        if self.llamadas:
            print("Lista de llamadas en espera de atención: ")
            for i, llamada in enumerate(self.llamadas, start=1):
                print(f"{i}. {llamada['nombre']} con motivo {llamada['motivo']}")
        else:
            print("No hay llamadas en espera")
        
def menu():
    cola = Cola()
    while True:
        print("\nPrograma de atención de llamadas")
        print("1. Agregar llamada a la cola")
        print("2. Atender llamada")
        print("3. Imprimir lista de llamadas")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            motivo = input("Ingrese el motivo de la llamada: ")
            cola.agregar(nombre, motivo)
        elif opcion == 2:
            cola.atender()
            print("llamada atendida")
        elif opcion == 3:
            cola.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción invalida, intentelo nuevamente")

if __name__ == "__main__":
    menu()