'''Comprobar si hay conexción directa entre dos nodos'''

grafo = {
    "1": ["2", "3"],
    "2": ["1", "4"],
    "3": ["1"],
    "4": ["2"]
}

def es_conexo(grafo, u, v):
    return u in grafo.get(v, [])

print(es_conexo(grafo, "1", "2"))
print(es_conexo(grafo, "1", "3"))
