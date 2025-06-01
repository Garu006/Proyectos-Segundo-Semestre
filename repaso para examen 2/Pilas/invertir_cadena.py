'''Escribe un programa que invierta el orden de los caracteres de una cadena usando una pila.
Por ejemplo, si ingresas "Hola Mundo", el programa debe devolver "dlroW olH".'''

class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
             return self.elementos.pop() 
        else:
            print("La pila esta vacia")
            return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0

def invertir(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

cadena = input("Ingrese un cadena: ")
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {invertir(cadena)}")
