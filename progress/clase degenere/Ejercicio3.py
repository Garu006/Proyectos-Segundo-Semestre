'''Paquete de algoritmos de busqueda
Desarrollar un programa para organizar diferentes algoritmos de busqueda en un paquete estructurado.
Los estudiantes deberan crear al menos dos modulos que contengan implementaciones de busqueda lineal y busqueda binaria, configurado adecuadamente el archivo init.py.
Posteriormente, desde un script principal, se utilizaran estas funciones para localizar elementos especificos en una coleccion de datos, 
resaltando la importancia de la organizacion en proyectos de mayor envergadura.'''


#hace una busqueda lineal para encontrar un elemento de la lista, si lo encuenta retornara el indice del elemento, si no hay un elemento en la lista, retornara -1
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busqueda_binaria(lista, elemento):
    i = 0
    final = len(lista) - 1

    while i <= final:
        mid = (i + final) // 2  # // Se utiliza para realizar una division y redondear al resultado mas cercano
        if lista[mid] == elemento:
            return mid
        elif lista[mid] < elemento:
            i = mid + 1
        else: 
            final = mid - 1
    return -1 #Retorna -1 si el elemento en la lista no se encuentra

if __name__ == "__main__":
    datos = [10,20,5,7,15,35,2]
    elementoa_buscar = 10

    resultado_lineal = busqueda_lineal(datos, elementoa_buscar)
    print(f"Busqueda lineal: El elemento fue encontrado en el indice {resultado_lineal}" if resultado_lineal != -1 else "Busqueda lineal: El elemento no fue encontrado")

    datos_ordenados = sorted(datos)
    print(f"Lista de datos ordenada para busqueda binaria: {datos_ordenados}")

    resultado_binario = busqueda_binaria(datos_ordenados, elementoa_buscar)
    print(f"Busqueda binaria: El elemento fue encontrado en el indice {resultado_binario}" if resultado_binario != -1 else "Busqueda binaria: Elemento no encontrado")
