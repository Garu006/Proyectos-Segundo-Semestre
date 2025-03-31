#Crear una clase producto con los siguientes atributos:
# codigo
# nombre
# precio

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    @property #lo que hace es que cuando lo llamemos, nos permita poner cualquier cosa
    def codigo(self):
        return self.codigo
    
#este codigo no esta terminado
