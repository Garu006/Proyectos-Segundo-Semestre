'''Una tienda con productos, carrito y funcionalidad para calcular el total'''

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - {self.precio}"