'''Gestion de productos e inventario
Diseñar una clase Producto que incluya atributos como codigo, nombre, precio y cantidad en stock.
Ademas que administre una coleccion de objetos Productos, incorporando metodos para agregar, buscar, actualizar y eliminar productos.
Este ejercicio permite modelar situaciones reales de gestion de ventas y refuerza el concepto de encapsualimiento y manejo de colecciones en programacion orientiada a objetos.'''

from clase_inventario import Inventario
from clase_producto import Producto

def main():
    inventario = Inventario()

    while True:
        print("\n-----Gestion de productos e inventario-----")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Mostrar productos")
        print("6. Salir")
        print("---------------------------------------------")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            codigo = int(input("Ingrese el codigo del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad en stock: "))

            producto = Producto(codigo, nombre, precio, stock)
            inventario.add_product(producto)

        elif opcion == "2":
            codigo = int(input("Ingrese el codigo del producto a buscar: "))
            producto = inventario.buscar_producto(codigo)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = int(input("Ingrese el codigo del producto a actualizar: "))
            print("Deje en blanco si desea no modificar ese campo.")
            nuevo_precio = input("Nuevo precio (actual: sin cambio): ")
            nuevo_stock = input("Nuevo stock (actual: sin cambio): ")

            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nuevo_stock = float(nuevo_stock) if nuevo_stock else None

            inventario.actualizar(codigo, nuevo_precio, nuevo_stock)

        elif opcion == "4":
            codigo = int(input("Ingrese el codigo del producto a eliminar: "))
            if inventario.delete_producto(codigo):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_productos()


        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opcion invalida. Intentelo denuevo.")

if __name__ == "__main__":
    main()



    