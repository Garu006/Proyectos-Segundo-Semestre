'''Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados. Use
una pila para realizar el seguimiento de los paréntesis abiertos.'''

class Pila:
    def __init__(self):
        self.pila = []

    def push(self, dato):
        self.pila.append(dato)
    
    def pop(self):
        if not self.estaVacio():
            return self.pila.pop()
        return None

    def estaVacio(self):
        return len(self.pila) == 0


def balancear(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}
    for caracter in cadena:
        if caracter in '([{':
            pila.push(caracter)
        elif caracter in ')]}':
            tope = pila.pop()
            if tope != pares[caracter]:
                return False
    return pila.estaVacio()


def main():
    while True:
        print("--- Menu ---")
        cadena = input("Ingrese una cadena o escriba salir para salir del programa: ")
        if cadena.lower() == "salir":
            break
        elif balancear(cadena):
            print("La cadena está balanceada.")
        else:
            print("Los paréntesis no están balanceados.")

if __name__ == "__main__":
    main()
