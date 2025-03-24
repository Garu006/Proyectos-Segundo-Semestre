'''Pide un numero de minutos y conviertelo a horas y minutos'''

mins = int(input("Ingrese un numerode minutos: "))
hours = mins // 60
minutos = mins % 60

print(f"{mins} minutos son {hours} horas y {minutos} minutos.")
