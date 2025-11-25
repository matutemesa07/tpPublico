# bubble_sort
items = []  # lista de numeros
n = 0    # cantidad de elementos
i = 0    # pasada actual
j = 0    # indice actual dentro de la pasada
swapped= False # para controlar si hubo intercambios

def init(vals):
    global items, n, i, j, swapped
    items = list(vals) # copiamos la lista original
    n = len(items)
    i = 0
    j = 0
    swapped= False

def step():
    """
    Hace un solo paso del algoritmo Bubble Sort.
    Devuelve qué comparación o intercambio se hizo.
    """
    global items, n, i, j, swapped

    # Si ya terminamos todas las pasadas, avisamos
    if i >= n - 1:
        return {"done": True}

    # Si j llegó al final de la pasada, reiniciamos y pasamos a la siguiente
    if j >= n - 1 - i:
        j = 0
        i = i + 1   # <-- reemplazado
        swapped = False
        # Si ya ordenamos todo
        if i >= n - 1:
            return {"done": True}

    # Comparamos los elementos vecinos
    a = j
    b = j + 1

    # Si están en el orden incorrecto, los intercambiamos
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]  # intercambio real
        j = j + 1   # <-- reemplazado
        return {"a": a, "b": b, "swap": True, "done": False}
    else:
        j = j + 1   # <-- reemplazado
        return {"a": a, "b": b, "swap": False, "done": False}