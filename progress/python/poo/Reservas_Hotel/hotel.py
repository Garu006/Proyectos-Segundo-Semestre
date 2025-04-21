'''Crear un sistema de reservas de habitaciones que permita gestionar la dsponibilidad.
Realizar reservas, cancelar y ver el estado de ocupacion.'''

from habitacion import Habitacion

class Hotel:
    def __init__(self):
        self.habitaciones = []

    def add_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def ver_habitaciones(self):
        for h in self.habitaciones:
            print(h)

    def reservar_habitacion(self, codigo):
        for h in self.habitaciones:
            if h.codigo == codigo:
                return h.reservar()
        return False

    def cancelar_reserva(self, codigo):
        for h in self.habitaciones:
            if h.codigo == codigo:
                return h.cancelar_reserva()
        return False
