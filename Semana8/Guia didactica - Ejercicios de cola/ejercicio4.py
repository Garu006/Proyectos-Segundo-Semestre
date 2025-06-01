'''Diseñe un programa que simule cómo un microprocesador atiende procesos en una cola de
ejecución. Cada proceso tiene un identificador, un nombre y una duración estimada en
milisegundos. A medida que el procesador queda libre, atiende al siguiente proceso en orden
de llegada (FIFO - First In, First Out). El sistema debe permitir agregar procesos a la cola,
mostrar el proceso en ejecución y visualizar los procesos pendientes. debe ser hecho con colas'''

class Proceso:
    def __init__(self):
        self.proceso = []

    def agregar(self, id, nombre, duracion):
        proceso = {
            "id": id,
            "nombre": nombre,
            "duración": duracion,
        }
        self.proceso.append(proceso)
        print(f"Se ha añadido el proceso {id} con nombre {nombre} y duración {duracion} a la cola")

    def procesar(self):
        if self.proceso:
            proceso = self.proceso.pop(0)
            print("Se ha procesado exitosamente")
        else:
            print("No hay procesos en la cola")
    
    def imprimir(self):
        if self.proceso:
            proceso = self.proceso[0]
            print(f"Se esta procesando el proceso {proceso['id']} con nombre {proceso['nombre']}")
        else:
            print("No hay procesos en la cola")
    
    def vacia(self):
        return len(self.proceso) == 0

def main():
    proceso = Proceso()
    while True:
        print("\nMicroprocesador de procesos")
        print("1. Agregar proceso a la cola")
        print("2. Procesar")
        print("3. Mostrar proceso en ejecución")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            id = int(input("Ingrese el id del proceso: "))
            nombre = input("Ingrese el nombre del proceso: ")
            duracion = int(input("Ingrese la duración estimada del proceso en milisegundos: "))
            proceso.agregar(id, nombre, duracion)
        elif opcion == 2:
            proceso.procesar()
        elif opcion == 3:
            proceso.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opción invalida, intentelo nuevamente")

if __name__ == "__main__":
    main()