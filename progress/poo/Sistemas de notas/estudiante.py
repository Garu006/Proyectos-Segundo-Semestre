class Estudiante:
    def __init__(self, nombre, apellido, cif):
        self._nombre = nombre
        self._apellido = apellido
        self._cif = cif
        self._notas = []

    def get_nota(self, nota):
        if 0 <= nota <= 100:
            self._notas.append(nota)
        else:
            print("La nota introducida no es valida")

    def calcular_promedio(self):
        if self._notas:
            return sum(self._notas) / len(self._notas)
        return 0

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        print(f"Nombre: {self._nombre}")
        print(f"Apellido: {self._apellido}")
        print(f"Cif: {self._cif}")
        print(f"Promedio: {promedio:.2f}")
