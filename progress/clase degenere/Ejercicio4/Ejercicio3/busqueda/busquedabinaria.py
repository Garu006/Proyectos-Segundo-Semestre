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
