'''Gestiona libros y prestamos entre usuarios'''

from biblio import Biblioteca
from libro import Libro
from usuario import Usuario

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("--- Gestion de libros ---")
        print("1. Agregar libro")
        print("2. Agregar usuario")
        print("3. Mostrar libros")
        print("4. Prestar  libro")
        print("5. Devolver libro")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            isbn = input("ISBN del libro: ")
            precio = float(input("Precio del libro: "))
            libro = Libro(titulo, autor, isbn, precio)
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente")

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre)
            biblioteca.agregar_usuario(usuario)
            print("Usuario agregado exitosamente")

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            isbn = input("IBSN del libro a prestar: ")
            usuario = input("Nombre del usuario: ")
            biblioteca.prestar_libro(isbn, usuario)
            print("Libro prestado")
        
        elif opcion == "5":
            isbn = input("IBSN del libro a devolver: ")
            usuario = input("Nombre del usuario: ")
            biblioteca.devolver_libro(isbn, usuario)
            print("libro devuelto")

        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida, intentelo de nuevo")

if __name__ == "__main__":
    main()
