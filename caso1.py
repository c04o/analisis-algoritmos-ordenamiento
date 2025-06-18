def insertion_sort(calificaciones):
    for i in range(1, len(calificaciones)):
        actual = calificaciones[i]
        j = i - 1
        while j >= 0 and calificaciones[j] > actual:
            calificaciones[j + 1] = calificaciones[j]
            j -= 1
        calificaciones[j + 1] = actual
    return calificaciones

# Lista de calificaciones de 30 estudiantes
calificaciones = [75, 60, 85, 90, 70, 55, 95, 80, 65, 100,
                  72, 68, 88, 74, 93, 62, 78, 96, 69, 58,
                  81, 77, 59, 84, 91, 66, 73, 87, 61, 89]

# Ordenar de menor a mayor
calificaciones_ordenadas = insertion_sort(calificaciones)

# Mostrar el resultado
print("Calificaciones ordenadas:", calificaciones_ordenadas)
