'''Imagina un servidor de archivos en una red donde varios usuarios solicitan acceso a un mismo
archivo compartido para su lectura. Para evitar conflictos o bloqueos, las solicitudes se atienden
en el orden en que llegan. Diseña un programa en Python que simule este comportamiento
utilizando una cola. El programa debe permitir registrar solicitudes de acceso (nombre del
usuario y archivo solicitado), mostrar qué usuario está accediendo al archivo y eliminar la
solicitud una vez atendida. También debe permitir consultar la lista de solicitudes pendientes.'''

class Servidor:
    def __init__(self):
        self.solicitudes = []
    
    def agregar(self, nombre, archivo):
        solicitud = {
            "nombre": nombre,
            "archivo": archivo,
        }
        self.solicitudes.append(solicitud)
        print(f"Se ha añadido la solicitud de {nombre} para el archivo {archivo} a la cola")

    def procesar(self):
        if self.solicitudes:
            solicitud = self.solicitudes.pop(0)
            print(f"Se ha procesado la solicitud de {solicitud['nombre']} para el archivo {solicitud['archivo']}")
        else:
            print("No hay solicitudes pendientes")
    
    def imprimir(self):
        if self.solicitudes:
            print("Lista de solicitudes pendientes: ")
            for i, solicitud in enumerate(self.solicitudes, start=1):
                print(f"{i}. Solicitud de {solicitud['nombre']} para el archivo {solicitud['archivo']}")
        else:
            print("No hay solicitudes pendientes")

    def vacia(self):
        return len(self.solicitudes) == 0

def main():
    server = Servidor()
    while True:
        print("\nPrograma de atención de solicitudes")
        print("1. Agregar solicitud a la cola")
        print("3. Mostrar solicitud pendiente")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del usuario: ")
            archivo = input("Ingrese el nombre del archivo: ")
            server.agregar(nombre, archivo)
        elif opcion == 2:
            server.procesar()
        elif opcion == 3:
            server.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción invalida, intentelo nuevamente")

if __name__ == "__main__":
    main()