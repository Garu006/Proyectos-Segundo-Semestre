from claseestudiante import ClaseEstudiante

def add_gasto(categorias, gastos):
    fecha = input("Fecha (dd/mm/aaaa): ")
    categoria = input("Categoría: ")
    if categoria not in categorias:
        print("Categoría no registrada. Por favor, registre la categoría primero.")
        return
    monto = float(input("Monto del gasto: "))
    descripcion = input("Descripción: ")
    gasto = ClaseEstudiante(fecha, categoria, monto, descripcion)
    gastos.append(gasto)
    print("El gasto ha sido registrado.")
