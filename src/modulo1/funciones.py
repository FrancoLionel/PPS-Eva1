def esBinario(strbinario):
    """
    Devuelve True si la cadena contiene solo caracteres '0' o '1'.
    En caso contrario, devuelve False.
    """
    for c in strbinario:
        if c not in "01":
            return False
    return True
