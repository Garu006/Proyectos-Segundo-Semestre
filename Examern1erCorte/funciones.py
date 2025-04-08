from claseestudiante import ClaseEstudiante

def total_gastomensual(gastos):
    total = sum(g.monto for g in gastos)
    print(f"El total gastado en el mes es: ${total:.2f}")

def total_por_categoria(categorias, lista_gasto):
    print("Total por categoría:")
    for categoria in categorias:
        total = sum(g.monto for g in lista_gasto if g.categoria == categoria)
        print(f"{categoria}: ${total:.2f}")

def listar_gastos(lista_gasto):
    print("Lista de todos los gastos:")
    for gasto in lista_gasto:
        print(gasto)
