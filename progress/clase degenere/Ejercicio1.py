'''Analisis de datos de ventas
Desarrollar un programa que procede un conjunto de registros de ventas (por ejemplo, listas de diccionarios) para extraer informacion relevante.
Los estudiantes deberan aplicar funcionees internas como map, filter y reduce para transformar y filtrar los datos, calculando totales y promedios.
Este ejercicio busca que los estudiantes identifiquen y aprovechen las funcionalidades nativas de Python para la manipulacion eficiente de estructuras de datos.'''


from functools import reduce   #reduce es una funcion que sirve para reducir una lista a un solo valor aplicando una funcion de manera acumulativa
#Lista de diccionarios con las ventas
ventas = [ # ventas es un diccionario, cada diccionario representa una venta
    {"producto": "Shampoo", "cantidad": 3, "precioUnitario": 300},
    {"producto": "Televisor", "cantidad": 1, "precioUnitario": 3000},
    {"producto": "Laptop", "cantidad": 1, "precioUnitario": 1000},
]
#Calcular el total de cada venta
ventasTotales = list(map(lambda venta: venta["cantidad"] * venta["precioUnitario"], ventas)) #map recorre la lista ventas y transforma cada elemento usando una funcion lambda
                                                                                 #la funcion multiplica cantidad por el precio unitario para calcular el total de cada venta y list convierte el resultado en una lista.
#Filtrar las ventas mayores a 100
ventasMayores100 = list(filter(lambda total: total > 100, ventasTotales)) #filter toma una funcion que devuelve true o false y la aplica a cada elemento de ventasTotales, si la venta es mayor a 100 la mantiene en la lista, sino no

#calcular el total de ventas
totalVentas = reduce(lambda acumulador, venta: acumulador + venta, totalVentas, 0) #reduce la lista de ventas totales a un solo valor

#calcular el promedio de las ventas
promedio =  totalVentas / len(ventasTotales) if totalVentas else 0 #se calcula el promedio de ventas diviciendo el total de las ventas entre el numero de ventas y si no hay ventas devolvera 0

#resultados
print("Ventas totales: ", ventasTotales)
print("Ventas mayores a 100: ", ventasMayores100)
print("Total de cada venta: ", totalVentas)
print("Promedio: ", promedio)
