'''Desarrollar un programa que permita al usuario gestionar una cuenta bancaria.
 El programa debera utilizar un menu que permita realizar diferentes operaciones sobre el saldo de la cuenta'''

saldo = 0.0

def menu():
    print("\n========== Gestion de cuenta bancaria ==========")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. salir")
    print("=====================================================")


def consult_saldo(saldo):
    print(f"\nTu saldo actual es de: ${saldo:.2f}")


def depo_money():
    global saldo 
    try: 
        cantidad = float(input("Ingresa la cantidad de dinero que va a depositar: "))
        if cantidad > 0:
            saldo += cantidad
            print(f"Deposito exitoso. Su saldo se ha actualizado a: ${saldo:.2f}")
        else:
            print("La cantidad a depositar debe de ser mayor a 0.")
    except ValueError:
        print("Invalido, intentelo nuevamente.")    


def reti_money():
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > 0:
            if cantidad <= saldo:
                saldo -= cantidad
                print(f"Retiro exitoso, su saldo se ha actualizado a: ${saldo:.2f}")
            else: 
                print("Fondos insuficientes.")
        else:
            print("La cantidad debe de ser mayor a 0.")
    except ValueError:
        print("Invalido, Intentelo nuevamente.")        

while True: 
    menu()
    option = input("Seleccione una opcion: ")
    if option == '1':
        consult_saldo(saldo)
    elif option == '2':
        depo_money()
    elif option == '3':
        reti_money()
    elif option == '4':
        print("Saliendo...")
        break
    else:
        print("Opcion invalida, intente nuevamente.")
