'''programa de atencion al cliente'''
class Clinica:
    def __init__(self):
        self.pacientes = []

    def registrar(self, nombre):
        self.pacientes.append(nombre)

    def atender(self):
        if self.pacientes:
            atendido = self.pacientes.pop(0)
            print(f"El paciente {atendido} ha sido aendido")
        else:
            print("No hay pacientes en espera")

    def imprimir(self):
        if self.pacientes:
            print("Lista de pacientes en espera de atención:")
            for i, paciente in enumerate(self.pacientes, start=1):
                print(f"{i}. {paciente}")

def menu():
    clinica = Clinica()
    while True:
            print("Programa de atencion al cliente")
            print("1. Registrar paciente")
            print("2. Atender paciente")
            print("3. Imprimir lista de pacientes")
            print("4. salir")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                nombre = input("Ingrese el nombre del paciente: ")
                clinica.registrar(nombre)
            elif opcion == 2:
                clinica.atender()
            elif opcion == 3:
                clinica.imprimir()
            elif opcion == 4:
                print("Saliendo del programa")
                break
            else:
                print("Opcion invalida, intentelo nuevamente")

if __name__ == "__main__":
    menu()