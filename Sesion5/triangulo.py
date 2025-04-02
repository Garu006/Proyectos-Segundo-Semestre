'''Desarrollar un programa que cargue los datos de un triangulo.
 Implementar un metodo/funcion para determinar el tipo de triangulo (equilatero, isosceleso escaleno)'''

#Programa principal
def triangulo():
    lista = []
    lado1 = int(input("ingrese la medida del lado 1: "))
    lado2 = int(input("ingrese la medida del lado 2: "))
    lado3 = int(input("ingrese la medida del lado 3: "))

    if lado1 == lado2 == lado3:
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")

def main():
    triangulo()

if __name__  == "__main__":
    main()