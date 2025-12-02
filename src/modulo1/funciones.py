def esBinario(strbinario):
    """
    Devuelve True si la cadena contiene solo caracteres '0' o '1'.
    En caso contrario, devuelve False.
    """
    for c in strbinario:
        if c not in "01":
            return False
    return True

def estaEnRango(valor, minimo, maximo):
    """
    Devuelve True si 'valor' está entre 'minimo' y 'maximo' (incluidos).
    """
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    """
    Devuelve True si 'valor' está dentro de la 'lista'.
    """
    return valor in lista
