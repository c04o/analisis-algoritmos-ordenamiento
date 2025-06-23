import matplotlib.pyplot as plt

def insertion_sort(calificaciones):
    count = 0
    for i in range(1, len(calificaciones)):
        actual = calificaciones[i]
        j = i - 1
        while j >= 0:
            count += 1  # Contar cada comparación
            if calificaciones[j] > actual:
                calificaciones[j + 1] = calificaciones[j]
                j -= 1
            else:
                break
        calificaciones[j + 1] = actual
    return calificaciones, count

# Generar datos para la gráfica
n_values = list(range(10, 1010, 10))  # Tamaños de lista de 10 a 1000

# Mejor caso: lista ya ordenada
counts_mejor = []
for n in n_values:
    lista_mejor = list(range(1, n+1))
    _, count = insertion_sort(lista_mejor)
    counts_mejor.append(count)

# Peor caso: lista ordenada en orden inverso
counts_peor = []
for n in n_values:
    lista_peor = list(range(n, 0, -1))
    _, count = insertion_sort(lista_peor)
    counts_peor.append(count)

# Curvas teóricas exactas
teorico_mejor = [n - 1 for n in n_values]
teorico_peor = [(n - 1) * n / 2 for n in n_values]

# Graficar
plt.plot(n_values, counts_mejor, 'o', label='Mejor caso (empírico)', color='green')
plt.plot(n_values, teorico_mejor, '--', label='Mejor caso: n-1', color='green')
plt.plot(n_values, counts_peor, 'o', label='Peor caso (empírico)', color='red')
plt.plot(n_values, teorico_peor, '--', label='Peor caso: (n-1)n/2', color='red')
plt.xlabel('Tamaño de la lista (n)')
plt.ylabel('Número de comparaciones')
plt.title('Complejidad de Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()

# Probar con la lista original
calificaciones = [75, 60, 85, 90, 70, 55, 95, 80, 65, 100,
                  72, 68, 88, 74, 93, 62, 78, 96, 69, 58,
                  81, 77, 59, 84, 91, 66, 73, 87, 61, 89]
calificaciones_ordenadas, comparisons = insertion_sort(calificaciones)
print(f"Calificaciones ordenadas: {calificaciones_ordenadas}")
print(f"Número de comparaciones para n={len(calificaciones)}: {comparisons}")
