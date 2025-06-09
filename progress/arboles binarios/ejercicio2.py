'''Crear y mostrar un grafo no dirigido'''
#Representacion de grafo no dirigido
grafo = {
    "Gabo": ["Joaquin", "Dani", "val"],
    "Joaquin": ["Gabo", "Dani", "val"],
    "val": ["Gabo", "Joaquin", "Dani"],
    "Dani": ["Joaquin", "val", "Gabo"]
}
#Conexiones
for nodo in grafo:
    print(f"{nodo} conectado con: {grafo[nodo]}")