import random
import time
import matplotlib.pyplot as plt

def insertion_sort(lista):
    count = 0
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0:
            count += 1  # Contar cada comparación
            if lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = actual
    return lista, count

def merge(left, right):
    result = []
    count = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        count += 1  # Contar cada comparación
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

def merge_sort(lista):
    if len(lista) <= 1:
        return lista, 0
    mid = len(lista) // 2
    left, left_count = merge_sort(lista[:mid])
    right, right_count = merge_sort(lista[mid:])
    merged, merge_count = merge(left, right)
    total_count = left_count + right_count + merge_count
    return merged, total_count

# Medir tiempo de ordenamiento para una lista de 10,000 números aleatorios
lista_grande = [random.randint(1, 10000) for _ in range(10000)]

# Tiempo para Insertion Sort
start_time = time.time()
insertion_sort(lista_grande.copy())
end_time = time.time()
duration_insertion = end_time - start_time
print(f"Tiempo de ordenamiento para Insertion Sort (10,000 números aleatorios): {duration_insertion:.4f} segundos")

# Tiempo para Merge Sort
start_time = time.time()
merge_sort(lista_grande.copy())
end_time = time.time()
duration_merge = end_time - start_time
print(f"Tiempo de ordenamiento para Merge Sort (10,000 números aleatorios): {duration_merge:.4f} segundos")

# Generar datos para la gráfica
n_values = list(range(10, 1010, 10))
counts_insertion = []
counts_merge = []

for n in n_values:
    lista = [random.randint(1, 10000) for _ in range(n)]
    _, count_insertion = insertion_sort(lista.copy())
    _, count_merge = merge_sort(lista.copy())
    counts_insertion.append(count_insertion)
    counts_merge.append(count_merge)

# Graficar
plt.plot(n_values, counts_insertion, 'o', label='Insertion Sort (random)', color='blue')
plt.plot(n_values, counts_merge, 'o', label='Merge Sort (random)', color='green')
plt.xlabel('Tamaño de la lista (n)')
plt.ylabel('Número de comparaciones')
plt.title('Comparación de Complejidad: Insertion Sort vs Merge Sort')
plt.legend()
plt.grid(True)
plt.show()
