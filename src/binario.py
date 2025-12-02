from modulo1.funciones import esBinario

if __name__ == "__main__":
    num = input("Introduce un número binario: ")

    if esBinario(num):
        decimal = int(num, 2)
        print(f"Su número decimal es: {decimal}")
    else:
        print("No es un número binario, pruebe de nuevo")
