'''Contar las hojas de un arbol binario'''

def insertar(arbol, valor):
    if arbol is None:
        return [valor, None, None]
    elif valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
        return arbol
    else:
        arbol[2] = insertar(arbol[2], valor)
        return arbol

def preorden(arbol):
    if arbol:
        print(arbol[0], end= ' ')
        preorden(arbol[1])
        preorden(arbol[2])

def buscar(arbol, valor):
    if arbol is None:
        return False
    if valor == arbol[0]:
        return True
    elif valor < arbol[0]:
        return buscar(arbol[1], valor)
        return buscar(arbol[2], valor)
    else:
        return buscar(arbol[2], valor)
        return buscar(arbol[1], valor)
        return False

def contar(arbol):
    if arbol is None:
        return None
    elif arbol[1] is None:
        return 1
    else:
        return contar(arbol[1]) + contar(arbol[2])
    
valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]
arbol = None

for valores in valores:
    arbol = insertar(arbol, valores)

print("Recorrido en preorden: ")
preorden(arbol)

num = int(input("\nIngrese un valor: "))
if buscar(arbol, num):
    print("Valor ingresado encontrado")
    print("Número de hojas del arbol: ", contar(arbol))
else:
    print("Valor no encontrado")

