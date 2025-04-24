'''Una tienda con productos, carrito y funcionalidad para calcular el total'''

from producto import Producto

class Tienda:
    def __init__(self):
        self.catalogo = [
            Producto("Monitor", 150.00),
            Producto("Laptop", 200.00),
            Producto("Teclado", 100.00),
            Producto("Mouse", 50.00),
            Producto("Cable USB", 10.00),
            Producto("Juegos", 30.00),
            Producto("Accesorios", 10.00),
            Producto("Pantalla", 50.00),
            Producto("Disco duro", 100.00),
            Producto("Tarjeta de crédito", 50.00),
            Producto("Caja fuerte", 10.00),
            Producto("Juego de mesa", 10.00),
        ]

    def mostrar_catalogo(self):
        for i, producto in enumerate(self.catalogo):
            print(f"{i+1}. {producto}")

    def obtener_producto(self, indice):
        if 0 <= indice < len(self.catalogo):
            return self.catalogo[indice]
        return None