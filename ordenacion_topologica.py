def ordenacion_topologica(n, restricciones):
    # Creamos un diccionario para almacenar el grado de entrada de cada tarea
    grado_entrada = {i: 0 for i in range(1, n+1)}
    # Creamos un diccionario para almacenar las tareas dependientes de cada tarea
    dependencias = {i: [] for i in range(1, n+1)}

    # Calculamos el grado de entrada y las dependencias de cada tarea
    for i, j in restricciones:
        grado_entrada[j] += 1
        dependencias[i].append(j)

    # Inicializamos una lista para almacenar las tareas sin dependencias
    tareas_sin_dependencias = [i for i in range(1, n+1) if grado_entrada[i] == 0]
    # Inicializamos una lista para almacenar el orden topológico resultante
    orden = []

    # Realizamos la ordenación topológica
    while tareas_sin_dependencias:
        tarea = tareas_sin_dependencias.pop()
        orden.append(tarea)
        # Disminuimos el grado de entrada de las tareas dependientes
        for dependiente in dependencias[tarea]:
            grado_entrada[dependiente] -= 1
            # Si el grado de entrada llega a cero, agregamos la tarea a la lista de tareas sin dependencias
            if grado_entrada[dependiente] == 0:
                tareas_sin_dependencias.append(dependiente)

    # Si no se pueden cumplir todas las restricciones, no hay ordenación posible
    if len(orden) != n:
        return None
    else:
        return orden

# Ejemplo
n = 6
restricciones = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (3, 6)]
orden = ordenacion_topologica(n, restricciones)
if orden is None:
    print("No se puede cumplir con todas las restricciones.")
else:
    print("Orden topológico de las tareas:", orden)
