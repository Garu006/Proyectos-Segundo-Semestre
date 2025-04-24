'''Una tienda con productos, carrito y funcionalidad para calcular el total'''

from tienda.producto import Producto

class Tienda:
    def __init__(self):
        self.catalogo = [
            Producto("Monitor", 150.00),
            Producto("Teclado", 100.00),
            Producto("Mouse", 50.00),
        ]

    def mostrar_catalogo(self):
        for i, producto in enumerate(self.catalogo, star = 1):
            print(f"{i+1}, {producto}")
    
    def obtener_producto(self, indice):
        if 0 <= indice < len(self.catalogo):
            return self.catalogo[indice]
        return None