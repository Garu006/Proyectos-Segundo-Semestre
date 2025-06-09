'''Recorrido en anchura'''

from collections import deque

def bfs(grafo, inicio):
    visitado = set()
    cola = deque([inicio])
    
    while cola: 
        nodo = cola.popleft()
        if nodo not in visitado:
            print(nodo, end=' ')
            visitado.add(nodo)
            cola.extend(vecino for vecino in grafo[nodo] if vecino not in visitado)

grafo = {
    "1": ["2", "3"],
    "2": ["1", "4"],
    "3": ["1"],
    "4": ["2"]
}

bfs(grafo, "1")