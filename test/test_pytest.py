import pytest

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

# Test esBinario
def test_esBinario_correcto():
    assert esBinario("1011")
    assert esBinario("0000")
    assert esBinario("111000111")
    assert esBinario("1")


def test_esBinario_incorrecto():
    assert not esBinario("10201")
    assert not esBinario("hola10")
    assert not esBinario("10 10")
    assert not esBinario("")
    assert not esBinario("!01")


def test_esBinario_input_erroneo():
    assert not esBinario(None)
    assert not esBinario(1010)
    assert not esBinario(["1", "0"])
    assert not esBinario(True)
    assert not esBinario(0.11)


# Test estaEnRango

def test_estaEnRango_correcto():
    assert estaEnRango(5, 1, 10)
    assert estaEnRango(1, 1, 10)
    assert estaEnRango(10, 1, 10)
    assert estaEnRango(7.5, 7.0, 8.0)
    assert estaEnRango(-1, -5, 0)


def test_estaEnRango_fuera():
    assert not estaEnRango(0, 1, 10)
    assert not estaEnRango(100, 1, 50)
    assert not estaEnRango(10.1, 0, 10)
    assert not estaEnRango(-10, -5, 5)


def test_estaEnRango_input_erroneo():
    assert not estaEnRango("5", 1, 10)
    assert not estaEnRango(5, "1", 10)
    assert not estaEnRango(5, 1, "10")
    assert not estaEnRango(None, 1, 10)
    assert not estaEnRango([], 0, 5)
    assert not estaEnRango(True, 0, 5)


# Test estaEnLista

def test_estaEnLista_presente():
    lista = ["manzana", 10, True, 4.5, (1, 2)]
    assert estaEnLista("manzana", lista)
    assert estaEnLista(True, lista)
    assert estaEnLista((1, 2), lista)


def test_estaEnLista_ausente():
    lista = ["coche", 2, 99, False]
    assert not estaEnLista("avion", lista)
    assert not estaEnLista(None, lista)
    assert not estaEnLista(500, lista)
    assert not estaEnLista([], lista)


def test_estaEnLista_input_erroneo():
    assert not estaEnLista(5, None)
    assert not estaEnLista("hola", 123)
    assert not estaEnLista({"a": 1}, ["a", "b"])
    assert not estaEnLista(None, None)