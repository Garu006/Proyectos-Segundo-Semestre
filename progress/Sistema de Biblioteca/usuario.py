class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def prestar_libros(self, libros):
        self.prestamos.append(libros)

    def devolver_libros(self, libros):
        if libros in self.prestamos:
            self.prestamos.remove(libros)
    
    def __str__(self):
        return f'Usuario: {self.nombre} - Libros prestados: {len(self.prestamos)}'

