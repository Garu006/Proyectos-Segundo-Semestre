def main():
    clase = Clase()

    while True:
        print("Seleccione una opcion: ")
        print("1. Agregar estudiante")
        print("2. Agregar nota de estudiante")
        print("3. Buscar estudiante por cif")
        print("4. Mostrar promedio de notas")
        print("5. Salir")

        opcion = input("Opcion: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            cif = input("Cif: ")


            #me dio paja, lo terminare luego