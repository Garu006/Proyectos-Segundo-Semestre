'''Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados envían documentos para ser impresos. 
Cada documento tiene un nombre, el usuario que lo envió y el número de páginas.
El sistema debe permitir agregar documentos a la cola, procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo actualmente.
Analice con los estudiantes como se evita el desorden en el uso compartido de un recurso limitado.'''

class ColaImpresion:
    def __init__(self):
        self.documentos = []
        
    #Enqueue: Agregar documento a la cola
    def addDocumento(self, nombre, usuario, paginas):
        documento = {
            "nombre": nombre,
            "usuario": usuario,
            "paginas": paginas
        }
        self.documentos.append(documento)
        print(f"Se ha añadido el documento {nombre} de {usuario} con {paginas} páginas a la cola")

    #Dequeue: Eliminar el primer documento de la cola (o el mas antiguo)
    def procesarDocumento(self):
        if self.documentos:
            documento = self.documentos.pop(0)
            print("Se ha procesado el documento")
        else:
            print("No hay documentos en la cola")

    def imprimirDocumento(self):
        if self.documentos:
            documento = self.documentos[0]
            print(f"Se está imprimiendo el documento {documento['nombre']} de {documento['usuario']})")
        else:
            print("No hay documentos en la cola")

    #Verificar si la cola está vacía
    def vacia(self):
        return len(self.documentos) == 0

def menu():
    cola = ColaImpresion()
    while True:
        print("\nCola de impresión de documentos")
        print("1. Agregar documento a la cola")
        print("2. Procesar documento")
        print("3. Mostrar documento en proceso")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del documento: ")
            usuario = input("Ingrese el nombre del usuario que lo envió: ")
            pagnas = int(input("Ingrese el número de páginas: "))
            cola.addDocumento(nombre, usuario, pagnas)
        elif opcion == 2:
            cola.procesarDocumento()
        elif opcion == 3:
            cola.imprimirDocumento()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentelo nuevamente")

if __name__ == "__main__":
    menu()
