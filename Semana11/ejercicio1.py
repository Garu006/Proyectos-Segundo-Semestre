'''ejercicio de grafo'''
#Representacion de grafo
grafo = {
    "Gabo": ["Niko, Joha, Steven"],
    "Niko": ["Gabo, Joha, Steven"],
    "Joha": ["Gabo, Niko, Steven"],
    "Steven": ["Joha, Niko, Gabo"]
}
#Conexiones
for nodo in grafo:
    print(f"{nodo} está conectado con: {', '.join(grafo[nodo])}")

