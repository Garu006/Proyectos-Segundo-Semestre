notafinal = list()
num_estudiantes = input("Ingrese la cantidad de estudiantes a evaluar: ")

for i in range (int(num_estudiantes)):
    notaFinal = input(f"Ingrese la cantidad de estudiantes {i+1}: ")
    if float(notaFinal) < 60:
        print("Reprobado.")
    elif float(notaFinal) >= 60 and float(notaFinal) <= 69:
        print("Regular.")
    elif float(notaFinal) >= 70 and float(notaFinal) <= 79:
        print("Bueno.")
    elif float(notaFinal) >= 80 and float(notaFinal) <= 89:
        print("Muy bueno.")  
    elif float(notaFinal) >= 90 and float(notaFinal) <= 100:
        print("Excelente.")  

print(f"Notas finales {notaFinal} ")                  