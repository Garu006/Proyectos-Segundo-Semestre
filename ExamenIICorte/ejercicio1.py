''' Inversión de palabras en una frase. Desarrolle un programa que utilice
una pila para invertir el orden de las palabras en una frase dada. Por ejemplo, la frase
"Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola".'''

class Pila:
    def __init__(self):
        self.pila = []
    
    def push(self, dato):
        self.pila.append(dato)

    def pop(self):
        return self.pila.pop()

    def estaVacio(self):
        return len(self.pila) == 0

    def estaLlena(self):
        return len(self.pila) > 0
    
    def invertir(self):
        palabras = []
        while not self.estaVacio():
            palabras.append(self.pop())
        return ' '.join(palabras)  # Devolver la frase invertida


def main():
    pila = Pila()
    while True:
        print("\n--- Menú ---")
        print("1. Añadir frase")
        print("2. Invertir frase")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            frase = input("Ingrese una frase: ")
            palabras = frase.split()  # Separa por espacios
            for palabra in palabras:
                pila.push(palabra)
            print("Frase añadida palabra por palabra.")
        
        elif opcion == 2:
            if pila.estaLlena():
                frase_invertida = pila.invertir()
                print("Frase invertida:", frase_invertida)
            else:
                print("La pila está vacía.")
        
        elif opcion == 3:
            print("Programa finalizado.")
            break
        
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()
