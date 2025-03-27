'''Crear un programa que simule la gestion de un inventario en una tienda.
Utilizar un menu para agregar, eliminar, modificar y consultar productos en el inventario.
Cada producto tendra un codigo, nombre, cantidad y precio'''

inventario = []

def menu():
    print("\n========== Menu de Gestion de Inventario ==========")
    print("1. Agregar producto")
    print("2. Eliminar Producto")
    print("3. Modificar Producto")
    print("4. consultar Producto")
    print("5. Ver productos")
    print("6. salir")
    print("=====================================================")

def Add_Product(inventario):
    codigo = input("Ingrese el codigo: ")
    nombre = input("Ingresa el nombre del producto: ")    
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio = float(input("Ingresa el precio: "))
    inventario.append({"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio })
    print("El producto ha sido agregado exitosamente.")
    
def Delete_Product(inventario):
    codigo = input("Ingrese el codigo del producto que desee eliminar: ")
    inventario[:] = [producto for producto in inventario if producto["codigo"] != codigo]
    print("El producto ha sido eliminado exitosamente.")

def Mod_product(inventario):
    codigo = input("Ingrese el codigo del producto que desea modificar: ")
    for producto in inventario:
        if producto["codigo"] == codigo:
            producto["nombre"] = input("Nuevo nombre: ")
            producto["cantidad"] = int(input("Nueva cantidad: "))
            producto["precio"] = float(input("Nuevo precio: "))
            print("Producto modificado exitosamente.")
            return
    print("El Producto que ingreso no encontrado")    

def Consult_product(inventario):
    codigo = input("Ingrese el codigo del producto que desee consultar: ")
    for producto in inventario:
        if producto["codigo"] == codigo:
            print(f"codigo: {producto['codigo']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio {producto['precio']}")
            return
    print("Producto no encontrado.")    

def Ver_products(inventario):
    if not inventario:
        print("La lista esta vacia.")
    else: 
        for producto in inventario:
            print(f"codigo: {producto['codigo']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio {producto['precio']}")    

while True:
    menu()
    option = input("Bienvenido, selecciona la opcion que prefieras: ")
    if option == '1':
         Add_Product(inventario)
    elif option == '2':
        Delete_Product(inventario)
    elif option == '3':
        Mod_product(inventario)
    elif option == '4':
        Consult_product(inventario)
    elif option == '5':
        Ver_products(inventario)
    elif option == '6':
        print("Saliendo...")
        break
    else: 
        print("opcion invalida")