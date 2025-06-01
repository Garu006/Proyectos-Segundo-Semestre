#Arbol Binario de Busqueda

def insertar(arbol, valor):
    if arbol is None:
        return [valor, None, None]
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    else:
        arbol[2] = insertar(arbol[2], valor)   
    return arbol



def preorden(arbol):
    if arbol is not None:
        print(arbol[0], end = ' ')
        preorden(arbol[1])
        preorden(arbol[2])



valores = [1,2,4,5,3,6,7,8,9,10]
arbol = None

for valor in valores:
    arbol = insertar(arbol, valor)

print("\nImpresion de elementos")
preorden(arbol)
