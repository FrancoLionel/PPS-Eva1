r"""
binario.py

Programa que determina si el valor dado dentro de un login
es correcto, aportando usuario y contraseña. En caso afirmativo,
se dará el nombre completo, en caso contrario, se pedirá de nuevo
un nombre de usuario.

Ultima Modificación. 02/12/2025
Autor. Franco Lionel Zalokar Elosegui
Dependencias. pytest

"""

from modulo1.funciones import estaEnRango, estaEnLista

usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

if __name__ == "__main__":
    max_intentos = 3
    intentos = 0

    lista_usuarios = list(usuarios.keys())

    while intentos < max_intentos:
        user = input("Usuario: ")

        if not estaEnLista(user, lista_usuarios):
            print("Usuario incorrecto.")
            intentos += 1
            continue

        password = input("Contraseña: ")

        if password == usuarios[user]["password"]:
            nombre = usuarios[user]["nombre"]
            apellido = usuarios[user]["apellido"]
            print(f"Bienvenido {nombre} {apellido}")
            break
        else:
            print("Contraseña incorrecta.")
            intentos += 1

    if estaEnRango(intentos, max_intentos, max_intentos):
        print("Has superado los 3 intentos.")
