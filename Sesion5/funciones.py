'''Ejercicios de funciones en python: suma, menor y mayor de los numeros'''
#definicion de funciones
def suma(lista):
    total = 0
    for x in lista:
        total = total + x
    return(total)

def menor(lista):
    men = lista[0]
    for x in lista:
        if x < men:
            men = x
    return(men)        

def mayor(lista):
    man = lista[0]
    for x in lista:
        if x > man:
            man = x
    return(man)        

#Programa principal
def main():
    #Captura de la cantidad de elementos
    lista = []
    print("Ingrese la cantidad de elementos a procesar: ", end = ' ')
    n = int(input())

    #Captura de datos
    for i in range(n):
        print(f"Ingrese el elemento {i+1}: ", end = ' ')
        num = int(input())
        lista.append(num)

        #llamado de las funciones
        print("Los elementos de la lista son: ", lista)
        print("La suma de todos los elementos es: ", suma(lista))
        print("El numero menor de la lista es: ", menor(lista))
        print("El numero mayor de la lista es: ", mayor(lista))

if __name__ == "__main__":
    main()