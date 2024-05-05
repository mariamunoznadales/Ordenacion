def ordenar_en_su_lugar(t):
    """
    Ordena la tabla 't' en su lugar.
    
    Args:
    - t: Una lista de elementos comparables.
    
    Returns:
    - La tabla 't' ordenada en su lugar.
    """
    for i in range(1, len(t)):
        j = i
        while j > 0 and t[j] < t[j - 1]:
            # Intercambiar t[j] con t[j - 1]
            t[j], t[j - 1] = t[j - 1], t[j]
            j -= 1
    return t

# Ejemplo
t = [4, 2, 7, 1, 5]
print("Tabla original:", t)
ordenar_en_su_lugar(t)
print("Tabla ordenada:", t)
