class Inventario:
    '''Clase para gestionar los productos'''
    def __init__(self):
        self.productos = {} #diccionario

    def add_product(self, producto): #Agrega un nuevo producto al inventario si no existe
        if producto.get_codigo() in self.productos:
            print(f"Error, ya eiste un producto con el codigo {producto.get_codigo()}")
            return False
        self.productos[producto.get_codigo()] = producto #Agrega el producto
        print(f"El producto ha sido agregado: {producto}")
        return True

    def buscar_producto(self, codigo): #Busca un producto segun su codigo
        return self.productos.get(codigo, None)


    def actualizar(self, codigo, nuevo_precio = None, nuevo_stock = None): #actualiza el stock o el precio de un producto existente
        producto = self.buscar_producto(codigo)
        if producto:
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            elif nuevo_stock is not None:
                producto.set_stock(nuevo_stock)
            print(f"Producto actualizado: {producto}")
            return True
        print(f"No se pudo actualizar el producto con el codigo {codigo}")
        return False
    
    def delete_producto(self, codigo):
        '''Elimina un producto segun el codigo ingresado'''
        if codigo in self.productos:
            producto_eliminado = self.productos.pop(codigo)
            print(f"Producto eliminado: {producto_eliminado}")
            return True #devuelve el valor bool true para indicar que es verdadero
        print(f"No se encontro el producto usando el codigo: {codigo}.")
        return False

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario esta vacio.")
        else:
            print("\n---Inventario---")
            for producto in self.productos.values():
                print(producto)