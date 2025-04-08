from hotel import Hotel
from habitacion import Habitacion

def main():
    hotel = Hotel()
    
    hotel.add_habitacion(Habitacion(101, "Simple", 50))
    hotel.add_habitacion(Habitacion(102, "Doble cama", 80))
    hotel.add_habitacion(Habitacion(103, "Suite", 100))
    hotel.add_habitacion(Habitacion(104, "Matrimonial", 120))

    while True:
        print("\nBienvenido al sistema de reservas del Hotel Masaya")
        print("1. Reservar habitación")
        print("2. Ver habitaciones")
        print("3. Cancelar reserva")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            codigo = int(input("Ingrese el número de habitación a reservar: "))
            if hotel.reservar_habitacion(codigo):
                print("Habitación reservada exitosamente.")
            else:
                print("No se pudo reservar la habitación.")

        elif opcion == '2':
            hotel.ver_habitaciones()

        elif opcion == '3':
            codigo = int(input("Ingrese el número de habitación a cancelar: "))
            if hotel.cancelar_reserva(codigo):
                print("Reserva cancelada.")
            else:
                print("No fue posible cancelar la reserva.")

        elif opcion == '4':
            print("Gracias por usar el sistema de reservas del Hotel Masaya.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


