'''Crear un sistema de reservas de habitaciones que permita gestionar la dsponibilidad.
Realizar reservas, cancelar y ver el estado de ocupacion.'''

class Habitacion:
    def __init__(self, codigo, tipo, precio):
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def cancelar_reserva(self):
        self.disponible = True
        return True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.codigo} - Tipo: {self.tipo}, Precio: ${self.precio} - {estado}"
