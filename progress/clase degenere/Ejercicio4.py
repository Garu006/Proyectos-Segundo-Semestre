'''Gestion de productos e inventario
Diseñar una clase Producto que incluya atributos como codigo, nombre, precio y cantidad en stock.
Ademas que administre una coleccion de objetos Productos, incorporando metodos para agregar, buscar, actualizar y eliminar productos.
Este ejercicio permite modelar situaciones reales de gestion de ventas y refuerza el concepto de encapsualimiento y manejo de colecciones en programacion orientiada a objetos.'''

class Producto:
    
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto (codigo = {self.codigo}, nombre {self.nombre}, precio {self.precio})"

