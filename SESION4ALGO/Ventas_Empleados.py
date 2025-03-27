'''Control de ventas de los empleados (3)
 de una emopresa de eltrodomesticos para un trismestre'''

#creacion  de listas
tablas_empleado = []
tabla_ventas = []
#este for sirve para llenar las tablas
for i in range(3):
    print(f"\nIngrese el nombre del empleado {i+1}: ", end = ' ')
    nombre = input()
    tablas_empleado.append(nombre)
#este for sirve para llenar las columnas
for fil in range(3):
    fila = [] 
    for col in range(3):
        print(f"\nIngrese la venta del empleado {fil+1} del mes {col+1}")
        ventas = float(input())
        fila.append(ventas)
    tabla_ventas.append(fila)
print("\nEmpleados: ", tablas_empleado)
print("\nVentas: ", tabla_ventas)

print("\nInformacion de ventas")
print("Nombre\tEnero\tFebrero\tMarzo")
for i, nombre in enumerate(tablas_empleado):
    print(f"{nombre}\t{tabla_ventas[i][0]:,.1f}\t{tabla_ventas[i][1]:,.1f}\t{tabla_ventas[i][2]:,.1f}\t")
