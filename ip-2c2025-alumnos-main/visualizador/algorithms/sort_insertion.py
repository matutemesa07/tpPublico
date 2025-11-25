# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)     # copio los valores
    n = len(items)         # guardo longitud
    i = 1                  # insertion empieza desde el segundo elemento
    j = None               # j todavía no arrancó


def step():
    global items, n, i, j

    # 1) Si ya procesé todos los elementos, termine
    if i >= n:
        return {"done": True}

    # 2) Si j es None, significa que recién vamos a empezar a insertar items[i]
    if j is None:
        j = i
        return {"a": j, "b": j-1 if j > 0 else j, "swap": False, "done": False}

    # 3) Si todavía puedo seguir desplazando hacia la izquierda…
    if j > 0 and items[j-1] > items[j]:
        # Hago UN swap adyacente
        items[j-1], items[j] = items[j], items[j-1]
        j = j-1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # 4) Si NO hay que seguir desplazando, paso al siguiente elemento
    i = i+1
    j = None
    return {"a": i-1, "b": i, "swap": False, "done": False}     