'''Agregar nodos y aristas con una clase'''

class Grafo:
    def __init__(self):
        self.adyacente = {}

    def agregar(self, nodo):
        if nodo not in self.adyacente:
            self.adyacente[nodo] = []

    def agregar_arista(self, a, b):
        if a in self.adyacente and b in self.adyacente:
            self.adyacente[a].append(b)

    def mostrar(self):
        for nodo in self.adyacente:
            print(f"{nodo}: {self.adyacente[nodo]}")

g = Grafo()
g.agregar("1")
g.agregar("2")
g.agregar("3")
g.agregar_arista("1", "2")
g.agregar_arista("1", "3")
g.mostrar()

