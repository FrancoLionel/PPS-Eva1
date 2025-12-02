import unittest

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

class TestFunciones(unittest.TestCase):

   class TestFunciones(unittest.TestCase):

    #TEST esBinario
    def test_esBinario_correcto(self):
        self.assertTrue(esBinario("1011"))
        self.assertTrue(esBinario("111000"))
        self.assertTrue(esBinario("0000"))
        self.assertTrue(esBinario("1"))

    def test_esBinario_incorrecto(self):
        self.assertFalse(esBinario("10201"))
        self.assertFalse(esBinario("binar10"))
        self.assertFalse(esBinario("10 10"))      
        self.assertFalse(esBinario(" 0101"))      
        self.assertFalse(esBinario("0101 "))      
        self.assertFalse(esBinario("10a01"))
        self.assertFalse(esBinario("!01"))
        self.assertFalse(esBinario(""))

    def test_esBinario_input_erroneo(self):
        self.assertFalse(esBinario(None))
        self.assertFalse(esBinario(1010))      
        self.assertFalse(esBinario(True))
        self.assertFalse(esBinario(["1", "0"]))
        self.assertFalse(esBinario(0.101))

    
    # Test estaEnRango
    def test_estaEnRango_dentro(self):
        self.assertTrue(estaEnRango(3, 1, 5))
        self.assertTrue(estaEnRango(100, 100, 200))
        self.assertTrue(estaEnRango(-2, -5, 0))
        self.assertTrue(estaEnRango(7.5, 7.0, 8.0))

    def test_estaEnRango_fuera(self):
        self.assertFalse(estaEnRango(0, 1, 5))
        self.assertFalse(estaEnRango(300, 100, 200))
        self.assertFalse(estaEnRango(-10, -5, 5))
        self.assertFalse(estaEnRango(10.1, 0, 10))

    def test_estaEnRango_input_erroneo(self):
        self.assertFalse(estaEnRango("5", 1, 10))   
        self.assertFalse(estaEnRango(None, 1, 10))
        self.assertFalse(estaEnRango([], 0, 5))
        self.assertFalse(estaEnRango(True, 0, 5))
        self.assertFalse(estaEnRango(5, "0", 10))
        self.assertFalse(estaEnRango(5, 0, "10"))

    # Test estaEnLista
    def test_estaEnLista_presente(self):
        lista = ["manzana", 10, True, 4.5, (1, 2)]
        self.assertTrue(estaEnLista("manzana", lista))
        self.assertTrue(estaEnLista(True, lista))
        self.assertTrue(estaEnLista((1, 2), lista))

    def test_estaEnLista_ausente(self):
        lista = ["coche", 2, 99, False]
        self.assertFalse(estaEnLista("avion", lista))
        self.assertFalse(estaEnLista(100, lista))
        self.assertFalse(estaEnLista(None, lista))
        self.assertFalse(estaEnLista([], lista))

    def test_estaEnLista_input_erroneo(self):
        self.assertFalse(estaEnLista(5, None))     
        self.assertFalse(estaEnLista("hola", 123)) 
        self.assertFalse(estaEnLista({"a":1}, ["a", "b"])) 
        self.assertFalse(estaEnLista(None, None))   


if __name__ == '__main__':
    unittest.main()