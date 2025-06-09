'''Grafo dirigido y añadir nodos'''

grafo = {}

def agregar_nodo(nodo):
    if nodo not in grafo:
        grafo[nodo] = set()
        print(f"nodo agregado al grafo: {nodo}")
        return True
    else:
        print(f"El nodo {nodo} ya no existe en el grafo")
        return False

def agregar_arista(origen, destino):
    if origen in grafo and destino in grafo:
        grafo[origen].add(destino)
        print(f"La arista {origen} con el nodo {destino} ha sido agregado")
        return True
    else:
        print(f"El nodo {origen} o {destino} no existen en el grafo")
        return False

agregar_nodo("yuca")
agregar_nodo("yatuzabe")
agregar_arista("yuca", "yatuzabe")
print(grafo)