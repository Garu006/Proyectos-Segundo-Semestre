'''Desarrollar un programa que se comporte como un diccionario ingles-Español; 
esto es, solicitara una palabra en ingle y escribira la correspondiente palabra en español. 
Para hacer mas sencillo el ejercicio, el numero de parejas de palabras estara limitado a 5. 
Por ejemplo, suponer que introducimos las siguientes parejas de palabras:

book libro
green verde
mouse raton

Una vez finalizada la introduccion de las listas de palabras, pasamos al modo traduccion, de forma que si introducimos green, la respuesta ha de ser verde.
Si la palabra no se encuentra, se emitira un mensaje que lo indique.

El programa constara de dos metodos, aparte de Main():
1. CrearDiccionario(). Este metodo creara el diccionario
2. traducir(). Este metodo realizara la labor de traduccion'''

#Codigo

diccionario = []

def menu():
    print("\n==========Bienvenido al diccionario Inglés-Español==========")
    print("1. Crear diccionario")
    print("2. Traducir palabra")
    print("3. Salir")
    print("============================================================")

def crearDiccionario():
    global diccionario  # Asegura que modificamos la variable global
    diccionario = []  # Reinicia la lista cada vez que se crea un nuevo diccionario

    while True:
        try:
            num1 = int(input("Ingrese la cantidad de pares de palabras a ingresar (máximo = 5): "))
            if 1 <= num1 <= 5:
                break
            else:
                print("El número que ingresó excede el máximo o es inválido, inténtelo de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")

    for i in range(num1):
        word = input(f"Ingrese la palabra {i+1} en inglés: ").strip().lower()
        palabra = input(f"Ingrese la palabra {i+1} en español: ").strip().lower()
        diccionario.append([word, palabra])  # Guarda el par de palabras

    return diccionario  # Retorna la lista completa

def traducir():
    palabra = input("Ingrese la palabra en inglés a traducir: ").strip().lower()

    for i in diccionario:
        if i[0] == palabra:
            print(f"La traducción de '{palabra}' es: {i[1]}")
            return

    print("La palabra que ingresaste no se encuentra en el diccionario.")

def main():
    while True:
        menu()
        option = input("Seleccione una opción: ")

        if option == '1':
            crearDiccionario()
        elif option == '2':
            if diccionario:
                traducir()
            else:
                print("Error, no hay ninguna palabra ingresada.")
        elif option == '3':
            print("Saliendo del programa...")
            break
        else:
            print("La opción que ingresó no es válida, vuelva a intentarlo.")

if __name__ == "__main__":
    main()