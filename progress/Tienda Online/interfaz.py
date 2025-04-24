'''Una tienda con productos, carrito y funcionalidad para calcular el total'''

from tienda.carrito import Carrito
from tienda.tienda import Tienda

def main():
    tienda = Tienda()
    carrito = Carrito()

    while True:
        print("---Bienvenido a la tienda online---")
        print("1. Mostrar catalogo")
        print("2. Comprar producto")
        print("3. Mostrar carrito")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            tienda.mostrar_catalogo()
        elif opcion == "2":
            indice = int(input("Ingrese el indice del producto: "))
            producto = tienda.obtener_producto(indice)
            if producto:
                carrito.agregar(producto)
                print(f"Producto agregado: {producto}")
            else:
                print("Opcion invalida")
        elif opcion == "3":
            print(carrito.mostrar_carrito())
            print(f"Total: {carrito.calcular_total()}")
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()