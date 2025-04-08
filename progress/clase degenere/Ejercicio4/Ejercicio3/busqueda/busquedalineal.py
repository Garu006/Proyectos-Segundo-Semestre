#hace una busqueda lineal para encontrar un elemento de la lista, si lo encuenta retornara el indice del elemento, si no hay un elemento en la lista, retornara -1
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1