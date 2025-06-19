'''Deteccion de ciclos en un grafo dirigido por un arbol binario.
Objetivo: Implementar un algoritmo para detectar si existe un ciclo en un grafo dirigido.
Requisitos:
Utiliza DFS.
Usa una pila de recursión (rec_stack) para detectar ciclos.'''


def dfs(grafo, v, rec_stack):
    if v in rec_stack:
        return True
    else:
        rec_stack.append(v)
        for u in grafo[v]:
            