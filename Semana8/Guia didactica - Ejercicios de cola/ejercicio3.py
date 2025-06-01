'''Implemente un sistema de turnos en una farmacia, donde los pacientes son atendidos en el
orden en que llegan. Cada paciente tiene un nombre y un tipo de servicio (compra, consulta,
receta). El sistema debe permitir registrar nuevos pacientes, atender al siguiente en la fila y
mostrar los turnos pendientes. debe ser con colas'''

class Cola:
    def __init__(self):
        self.Pacientes = []
    
    def agregar(self, nombre, tipo):
        paciente = {
            "nombre": nombre,
            "tipo": tipo,
            "turno": None,
        }
        self.Pacientes.append(paciente)
        print(f"Se ha añadido el paciente {nombre} con tipo {tipo} a la cola")
    
    def atender(self):
        if self.Pacientes:
            paciente = self.Pacientes.pop(0)
            print(f"Se ha atendido el paciente {paciente['nombre']} con tipo {paciente['tipo']}")
        else:
            print("No hay pacientes en la cola")
    
    def imprimir(self):
        if self.Pacientes:
            print("Lista de pacientes en espera de atención: ")
            for i, paciente in enumerate(self.Pacientes, start=1):
                print(f"{i}. {paciente['nombre']} con tipo {paciente['tipo']}")
            else:
                print("No hay pacientes en espera")

def main():
    cola = Cola()
    while True:
        print("\nPrograma de atención de pacientes")
        print("1. Agregar paciente a la cola")
        print("2. Atender paciente")
        print("3. Imprimir lista de pacientes")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del paciente: ")
            tipo = input("Ingrese el tipo de servicio: ")
            cola.agregar(nombre, tipo)
        elif opcion == 2:
            cola.atender()
            print("Paciente atendido")
        elif opcion == 3:
            cola.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción invalida, intentelo nuevamente")

if __name__ == "__main__":
    main()
