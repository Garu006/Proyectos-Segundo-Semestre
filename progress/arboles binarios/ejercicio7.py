'''grafo a profundidad'''

def dfs(grafo, nodo, visitado = None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo, end=' ')
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)

grafo = {
    "gabo": ["joha", "niko", "val"],
    "joha": ["gabo", "niko", "val"],
    "niko": ["gabo", "joha", "val"],
    "val": ["gabo", "joha", "niko"]
}

print("Conexiones del grafo: ")
for nodo in grafo:
    print(f"{nodo} esta conectado con: {grafo[nodo]}")

print("\nRecorrido en profundidad: ")
dfs(grafo, "gabo")