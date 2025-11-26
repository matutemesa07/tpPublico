items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"


def step():
    global items, n, i, j, min_idx, fase

    # Si ya está todo ordenado
    if i >= n:
        return {"done": True}

    # ------------------------- FASE 1: BUSCAR -------------------------
    if fase == "buscar":

        # Mientras j esté dentro del largo de la lista:
        if j < n:
            # Comparamos items[j] con el mínimo actual items[min_idx]
            a = min_idx
            b = j

            # Si encontramos un valor menor → actualizamos min_idx
            if items[j] < items[min_idx]:
                min_idx = j

            # Avanzamos j para el próximo paso
            j =j+ 1

            # Devolvemos, pero sin swap
            return {
                "a": a,
                "b": b,
                "swap": False,
                "done": False
            }

        # Si j == n, terminó el recorrido → pasamos a fase swap
        fase = "swap"

    # ------------------------- FASE 2: SWAP -------------------------
    if fase == "swap":
        # Si el mínimo real NO está en i → hacer ese único swap
        if min_idx != i:
            a = i
            b = min_idx

            # Hacemos el swap REAL en Python
            items[a], items[b] = items[b], items[a]

            # Luego de hacer el swap, avanzamos i
            # pero devolvemos primero el swap=True
            min_idx = i   # por claridad, aunque de inmediato reiniciamos
            fase = "post_swap"

            return {
                "a": a,
                "b": b,
                "swap": True,
                "done": False
            }

        # Si min_idx == i → no hay swap
        fase = "post_swap"

    # --------------------- FASE POST-SWAP / REINICIO ---------------------
    # Terminamos esta pasada para el índice i
    if fase == "post_swap":
        i += 1

        # Si terminamos la lista
        if i >= n:
            return {"done": True}

        # Reiniciar punteros para la nueva pasada
        j = i + 1
        min_idx = i
        fase = "buscar"

        # Devolver highlight mínimo para empezar la próxima búsqueda
        return {
            "a": i,
            "b": j if j < n else i,
            "swap": False,
            "done": False
        }
