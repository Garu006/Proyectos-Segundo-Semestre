'''Grafo no dirigo'''

grafo = {
    "gabo": ["joha", "niko", "val"],
    "joha": ["gabo", "niko", "val"],
    "niko": ["gabo", "joha", "val"],
    "val": ["gabo", "joha", "niko"]
}

for nodo in grafo:
    print(f"{nodo} esta conectado a: {grafo[nodo]}")