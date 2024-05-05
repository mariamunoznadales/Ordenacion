def ordenacion_por_insercion_dicotomica(t, inicio, fin):
    # Verificar precondiciones
    assert inicio <= fin
    assert inicio >= 0 and fin < len(t)

    # Algoritmo de ordenación por inserción dicotómica
    for i in range(inicio + 1, fin + 1):
        elemento = t[i]
        izquierda = inicio
        derecha = i - 1

        # Búsqueda binaria para encontrar la posición adecuada
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if elemento < t[medio]:
                derecha = medio - 1
            else:
                izquierda = medio + 1

        # Desplazar los elementos a la derecha para hacer espacio
        for j in range(i, izquierda, -1):
            t[j] = t[j - 1]

        # Insertar el elemento en la posición encontrada
        t[izquierda] = elemento

    # Verificar postcondiciones
    assert inicio == inicio
    assert fin == fin
    assert t[inicio: fin + 1] == sorted(t[inicio: fin + 1])

'''Este código sigue los principios del algoritmo de ordenación por inserción dicotómica.
Utiliza un ciclo para iterar sobre la tabla desde el segundo elemento hasta el último, empleando la búsqueda binaria para 
hallar la posición óptima de inserción de cada elemento. Posteriormente, desplaza los elementos hacia la derecha para crear espacio y,
por último, inserta el elemento en su posición correcta.'''