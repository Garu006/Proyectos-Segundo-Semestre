from categorias import add_categoria
from gastos import add_gasto
from funciones import total_gastomensual, total_por_categoria, listar_gastos
from promedio import promedio_por_categoria

def main():
    categorias = []  # Lista de categorías
    lista_gasto = []  # Lista de gastos

    while True:
        print("\n-----MENU DE CONTROL DE GASTOS-----")
        print("1. Agregar una nueva categoría")
        print("2. Agregar un gasto")
        print("3. Mostrar el total gastado en el mes")
        print("4. Mostrar el total por cada categoría")
        print("5. Listar todos los gastos")
        print("6. Mostrar el gasto promedio por categoría")
        print("7. Salir del programa")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            add_categoria(categorias)
        elif opcion == "2":
            add_gasto(categorias, lista_gasto)
        elif opcion == "3":
            total_gastomensual(lista_gasto)
        elif opcion == "4":
            total_por_categoria(categorias, lista_gasto)
        elif opcion == "5":
            listar_gastos(lista_gasto)
        elif opcion == "6":
            promedio_por_categoria(categorias, lista_gasto)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
