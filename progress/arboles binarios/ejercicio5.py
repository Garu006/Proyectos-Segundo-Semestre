'''Representacion con lista adyacente usando nodos'''

class Grafo:
    def __init__(self):
        self.adyacente = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.adyacente:
            self.adyacente[nodo] = []
            print(f"El nodo {nodo} ha sido agregado al grafo")
            return True
        else:
            print(f"El nodo {nodo} ya no existe en el grafo")
            return False
    
    def agregar_arista(self, origen, destino):
        if origen in self.adyacente and destino in self.adyacente:
            self.adyacente[origen].append(destino)
            print(f"La arista {origen} con el nodo {destino} ha sido agregado")
            return True
        else:
            print(f"El nodo {origen} o {destino} no existen en el grafo")
            return False
    
    def mostrar(self):
        print("Enlaces del grafo: ")
        for nodo in self.adyacente:
            print(f"{nodo} conectado con: {self.adyacente[nodo]}")

grafo = Grafo()
grafo.agregar_nodo("liendra")
grafo.agregar_nodo("yatuzabe")
grafo.agregar_arista("liendra", "yatuzabe")
grafo.mostrar()