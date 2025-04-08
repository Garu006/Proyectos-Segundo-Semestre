from claseestudiante import ClaseEstudiante

def promedio_por_categoria(categorias, lista_gasto):
    print("Promedio por categoría:")
    for categoria in categorias:
        gastos = [g.monto for g in lista_gasto if g.categoria == categoria]
        if gastos:
            promedio = sum(gastos) / len(gastos)
            print(f"{categoria}: {promedio:.2f}")
        else:
            print(f"{categoria}: No hay gastos registrados.")