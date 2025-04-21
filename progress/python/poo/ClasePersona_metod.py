'''Crea una clase que "persona" que tenga un nombre y una edad. 
Agrega un metodo para mostrar los datos'''

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

#Prueba de la clase
persona1 = persona("Gabriel", 19)
persona1.mostrar_datos()