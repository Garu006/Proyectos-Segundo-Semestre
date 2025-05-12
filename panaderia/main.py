#Aqui se importa la clase Pila y se crea un objeto pila
from Pila import Pila
pila = Pila()

#El menu se muestra en un bucle infinito que no terminara hasta que el usuario seleccione salir
while True:
    print("1. Agregar pan")
    print("2. Vender pan")
    print("3. Mostrar pan")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: ")) #El usuario selecciona una opcion
    if opcion == 1: #El pide el nombre del pan y lo añade a la pila usando el metodo "agregarPanes"
        pan = input("Ingrese el nombre del pan: ")
        pila.agregarPanes(pan)
    elif opcion == 2: #Se intenta vender un pan (el ultimo que entro)
        panVendido = pila.venderPan()
        if panVendido: #Si hay pan en la pila, se muestra cual se vendio
            print(f"Pan vendido: {panVendido}")
        else: #si no hay panes se muestra un mensaje de error
            print("No hay panes para vender.")
    elif opcion == 3:
        pila.mostrarPanes() #Simplemente llama al metodo "mostrarPanes" para ver el estado actual de la pila
    elif opcion == 4: #Finaliza el ciclo y el programa
        break
    else: #Si el usuario ingresa una numero diferente del 1 al 4, se muestra un mensaje de error
        print("Opción no válida. Intente de nuevo.")