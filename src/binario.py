r"""
binario.py

Programa que determina si una cadena es binario o no. En caso afirmativo
se calculará el decimal, por el contrario, se pedirá de nuevo un número.

Ultima Modificación. 02/12/2025
Autor. Franco Lionel Zalokar Elosegui
Dependencias. Unittest

"""
from modulo1.funciones import esBinario

if __name__ == "__main__":
    num = input("Introduce un número binario: ")

    if esBinario(num):
        decimal = int(num, 2)
        print(f"Su número decimal es: {decimal}")
    else:
        print("No es un número binario, pruebe de nuevo")
