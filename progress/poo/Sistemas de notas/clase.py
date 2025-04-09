class Clase:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiantes):
        self.estudiantes.append(estudiantes)

    def  buscar_por_cif(self, cif):
        for estudiante in self.estudiantes:
            if estudiante.cif == cif:
                return estudiante
        return None

    def mostrar_promedio(self):
        print("Pronedio de notas de los estudiantes: ")
        for estudiante in self.estudiantes:
            print(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Cif: {estudiante.cif}, Promedio: {estudiante.calcular_promedio():.2f}")
