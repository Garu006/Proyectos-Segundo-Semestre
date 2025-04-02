class Empleado:
    def __init__(self, nombre, salarioBruto):
        self.__nombre = nombre
        self.__salarioBruto = salarioBruto

    def get_Nombre(self):
        return self.__nombre
    
    def get_SalarioBruto(self):
        from Salario_neto import salarioNeto 
        return salarioNeto(self.__salarioBruto)         
        