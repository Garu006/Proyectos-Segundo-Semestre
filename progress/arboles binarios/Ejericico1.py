'''Crea un arbol binario insertando los siguientes valores
[8, 3, 10, 1, 6, 14, 4, 7, 13]
Muestra los valores del arbol en preorden'''

def insertar(arbol, valor):
    if arbol is None:
        return [valor, None, None]
    elif valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
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
    else:
        return buscar(arbol[2], valor)

def encontrar_min(arbol):
    actual = arbol
    while actual[1] is not None:
        actual = actual[1]
    return actual[0]

def encontrar_max(arbol):
    actual = arbol
    while actual[2] is not None:
        actual = actual[2]
    return actual[0]

def altura(arbol):
    if arbol is None:
        return 0
    return 1 + max(altura(arbol[1]), altura(arbol[2]))

def eliminar(arbol, valor):
    if arbol is None:
        return None
    elif valor < arbol[0]:
        arbol[1] = eliminar(arbol[1], valor)
    else:
        arbol[2] = eliminar(arbol[2], valor)

valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]
arbol = None

for valor in valores:
    arbol = insertar(arbol, valor)

print("Recorrido en preorden: ")
preorden(arbol)

num = int(input("\nIngrese un valor: "))
if buscar(arbol, num):
    print("Valor ingresado encontrado")
else:
    print("Valor no encontrado")

print("Mínimo: ", encontrar_min(arbol))
print("Mánimo: ", encontrar_max(arbol))

print("Altura del arbol: ", altura(arbol))

valor = int(input("\nIngrese el valor que desee eliminar: "))
eliminar(arbol, valor)
print("Valor eliminado")