import random

def quicksort(arr, left, right):
    if left < right:
        pivot_index = left
        pivot_value = arr[pivot_index]
        store_index = pivot_index + 1

        for i in range(pivot_index + 1, right + 1):
            if (arr[i] < pivot_value) or (arr[i] == pivot_value and random.randint(0, 1) == 0):
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        arr[pivot_index], arr[store_index - 1] = arr[store_index - 1], arr[pivot_index]

        new_pivot_index = store_index - 1

        quicksort(arr, left, new_pivot_index - 1)
        quicksort(arr, new_pivot_index + 1, right)

# Ejemplo de uso
arr = [5, 3, 8, 4, 2, 7, 1, 10, 6]
quicksort(arr, 0, len(arr) - 1)
print("Arreglo ordenado:", arr)