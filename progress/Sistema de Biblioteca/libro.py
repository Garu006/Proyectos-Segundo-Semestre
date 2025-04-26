class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.isbn = isbn
        self.disponible = True
    def __str__(self):
       estado = 'Disponible' if self.disponible else 'No disponible'
       return f'"{self.titulo}" de {self.autor} (ISBN: {self.isbn}) precio: {self.precio} - {estado}'
