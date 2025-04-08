'''Paquete de algoritmos de busqueda
Desarrollar un programa para organizar diferentes algoritmos de busqueda en un paquete estructurado.
Los estudiantes deberan crear al menos dos modulos que contengan implementaciones de busqueda lineal y busqueda binaria, configurado adecuadamente el archivo init.py.
Posteriormente, desde un script principal, se utilizaran estas funciones para localizar elementos especificos en una coleccion de datos, 
resaltando la importancia de la organizacion en proyectos de mayor envergadura.'''

from busqueda.busquedabinaria import busqueda_binaria
from busqueda.busquedalineal import busqueda_lineal

if __name__ == "__main__":
    datos = [10,20,5,7,15,35,2]
    elementoa_buscar = 10

    resultado_lineal = busqueda_lineal(datos, elementoa_buscar)
    print(f"Busqueda lineal: El elemento fue encontrado en el indice {resultado_lineal}" if resultado_lineal != -1 else "Busqueda lineal: El elemento no fue encontrado")

    datos_ordenados = sorted(datos)
    print(f"Lista de datos ordenada para busqueda binaria: {datos_ordenados}")

    resultado_binario = busqueda_binaria(datos_ordenados, elementoa_buscar)
    print(f"Busqueda binaria: El elemento fue encontrado en el indice {resultado_binario}" if resultado_binario != -1 else "Busqueda binaria: Elemento no encontrado")
