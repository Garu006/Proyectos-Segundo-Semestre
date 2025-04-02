from clase_empleado import Empleado

def main():
    empleados = []
    print("Ingrese la cantidad de los empleados: ", end = ' ')
    n = int(input())

    print("Ingrese los datos de los empleados: ")

    for i in range(n):
        print("Nombre: ", end = " ")
        nombre = input()
        print("Salario Bruto: ", end = " ")
        salarioBruto = float(input())
        emp = Empleado(nombre, salarioBruto)
        empleados.append(emp)

    print("Datos de Empleados: ")
    for emp in empleados:
        print(f"{emp.get_Nombre()}: {emp.get_SalarioBruto(): .2f}")

if __name__ == "__main__":
    main()
    