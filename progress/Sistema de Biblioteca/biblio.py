from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, libro, usuario):
        usuario = self.buscar_usuario(usuario)
        libro = self.buscar_libro(libro)
        if usuario and libro and libro.disponible:
            lbro.disponible = False
            usuario.prestar_libros(libro)
            print(f'libro "{libro.titulo}" prestado por {usuario.nombre}')
        else:
            print("Libro no disponible, no se puede realizar el prestamo")

    def devolver_libro(self, libro, usuario):
        usuario = self.buscar_usuario(usuario)
        libro = self.buscar_libro(libro)
        if usuario and libro in usuario.prestamos:
            libro.disponible = True
            usuario.devolver_libro(libro)
            print(f'Libro "{libro.titulo}" devuelto por {usuario.nombre}')
        else:
            print("No se puede realizar la devolucion")

    def buscar_libro(self, libro):
        for libro in self.libros:
            if libro.isbn == libro:
                return libro
        return None

    def buscar_usuario(self, usuario):
        for usuario in self.usuarios:
            if usuario.nombre == usuario:
                return usuario
        return None

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)