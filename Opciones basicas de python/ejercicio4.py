Nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = input("Ingrese la cantidad de horas que trabajo durante la semana: ")
tarifa = input("Ingrese la tarifa" )

if int(horas_trabajadas) <= 48:
    total = int(horas_trabajadas) * float(tarifa)
    print("el salario ganado por las horas trabajadas durante la semana es: {total}")
else:
    extra = input(horas_trabajadas) * float(tarifa) * 2
    print("El salario ganado por las horas trabajadas durante la semana es: {extra}")