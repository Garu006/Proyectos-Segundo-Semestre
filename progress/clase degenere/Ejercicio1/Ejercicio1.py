'''Analisis de datos de ventas
Desarrollar un programa que procede un conjunto de registros de ventas (por ejemplo, listas de diccionarios) para extraer informacion relevante.
Los estudiantes deberan aplicar funcionees internas como map, filter y reduce para transformar y filtrar los datos, calculando totales y promedios.
Este ejercicio busca que los estudiantes identifiquen y aprovechen las funcionalidades nativas de Python para la manipulacion eficiente de estructuras de datos.'''

ventas = [
    {"producto": "Laptop", "cantidad": 2, "precio_unitario": 1000},
    {"producto": "Mouse", "cantidad": 5, "precio_unitario": 20},
    {"producto": "Teclado", "cantidad": 3, "precio_unitario": 50},
    {"producto": "Monitor", "cantidad": 1, "precio_unitario": 300},
    {"producto": "Celular", "cantidad": 4, "precio_unitario": 800},
]  # Este módulo contiene los datos de ventas como una lista de diccionarios

from functools import reduce

def Calcular_total(ventas):
    '''Calculo el total de cada venta (cantidad * precio_unitario)'''
    return list(map(lambda venta: venta["cantidad"] * venta["precio_unitario"], ventas))

def VentasMayores100(ventasTotales, filtro=100):
    '''Filtra las ventas cuyo total sea mayor al filtro'''
    return list(filter(lambda total: total > filtro, ventasTotales))

def calcularTotal_Ventas(ventasTotales):
    '''Calcula la suma total de todas las ventas'''
    return reduce(lambda acc, venta: acc + venta, ventasTotales, 0)

def calcularPromedio(ventasTotales):
    '''Calcular el promedio de las ventas'''
    return calcularTotal_Ventas(ventasTotales) / len(ventasTotales) if ventasTotales else 0

# Calcular los totales de cada venta
ventasTotales = Calcular_total(ventas)

# Filtrar ventas mayores a 100
ventasMayores100 = VentasMayores100(ventasTotales, 100)

# Calcular el total de ventas
totalVentas = calcularTotal_Ventas(ventasTotales)

# Calcular el promedio de ventas
promedioVentas = calcularPromedio(ventasTotales)

# Mostrar resultados
print("Ventas Totales: ", ventasTotales)
print("Ventas Mayores a 100: ", ventasMayores100)
print("Total de ventas: ", totalVentas)
print("Promedio de ventas: ", promedioVentas)
