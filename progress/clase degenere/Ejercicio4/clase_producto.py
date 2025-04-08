class Producto:
    
    def __init__(self, codigo, nombre, precio, stock):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    #getters protege los atributos
    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_stock(self):
        return self._stock

    #setters solo se pueden modificar con metodos
    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock

    def __repr__(self):
        return f"Producto (codigo={self._codigo}, nombre={self._nombre}, precio={self._precio}, stock={self._stock})"
