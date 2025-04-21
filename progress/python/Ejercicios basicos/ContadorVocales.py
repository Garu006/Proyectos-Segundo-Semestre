frase = input("Ingrese una oracion: ").lower() #Se convierte todo a minusculas
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in frase:
        contador += 1

print("La cantidad de vocales en la oracion es: ", contador)