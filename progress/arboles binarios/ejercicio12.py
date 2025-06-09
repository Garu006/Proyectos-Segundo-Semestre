'''Verificar si dos arboles binarios son iguales'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def son_iguales(a, b):
    if not a and not b:
        return True
    if a and b and a.valor == b.valor:
        return son_iguales(a.izq, b.izq) and son_iguales(a.der, b.der)
    return False

#Arbol 1
a1 = Nodo(1)
a1.izq = Nodo(2)
a1.der = Nodo(3)

#Arbol 2
a2 = Nodo(1)
a2.izq = Nodo(2)
a2.der = Nodo(3)

print("¿Son iguales?", son_iguales(a1, a2))