import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Generar lista aleatoria
data = [random.randint(0, 100) for _ in range(50)]
states = []

# Almacenar el estado actual del arreglo
def record_state(arr, color_array):
    states.append((arr.copy(), color_array.copy()))

# Algoritmo quicksort
def quicksort(arr, low, high, color_array):
    if low < high:
        pivot_index = partition(arr, low, high, color_array)
        quicksort(arr, low, pivot_index - 1, color_array)
        quicksort(arr, pivot_index + 1, high, color_array)

def partition(arr, low, high, color_array):
    pivot = arr[low]
    pivot_index = low
    color_array[pivot_index] = "red"
    store_index = low + 1

    for i in range(low + 1, high + 1):
        color_array[i] = "blue"
        record_state(arr, color_array)

        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            color_array[i], color_array[store_index] = 'green', 'green'
            record_state(arr, color_array)
            store_index += 1

        color_array[i] = "gray"

    arr[low], arr[store_index - 1] = arr[store_index - 1], arr[low]
    color_array[low], color_array[store_index - 1] = 'green', 'green'
    record_state(arr, color_array)

    for i in range(len(arr)):
        if color_array[i] != "red":
            color_array[i] = "gray"
    return store_index - 1

# Preparar colores iniciales
color_array = ['gray'] * len(data)
record_state(data, color_array)
quicksort(data, 0, len(data) - 1, color_array)

# Configurar gráfica
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), data, color=color_array)
ax.set_title("Animación del algoritmo Quicksort")
ax.set_ylim(0, max(data) + 10)

# Función para actualizar la animación
def update(i):
    arr, colors = states[i]
    for rect, h, c in zip(bar_rects, arr, colors):
        rect.set_height(h)
        rect.set_color(c)

ani = animation.FuncAnimation(fig, update, frames=len(states), interval=100, repeat=False)
plt.show()
