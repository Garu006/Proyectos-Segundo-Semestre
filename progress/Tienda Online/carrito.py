'''Una tienda con productos, carrito y funcionalidad para calcular el total'''

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p.precio for p in self.productos)

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito esta vacio")
        return '\n',join(str(p) for p in self.productos)