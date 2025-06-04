# Representación del grafo como diccionario
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

# Mostrar conexiones
for nodo in grafo:
    print(f"{nodo} está conectado con: {', '.join(grafo[nodo])}")
