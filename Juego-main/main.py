from funciones.entidades import *
from funciones.func import *

personaje = generar_personaje(input("Ingresa el nombre: "))

class Exception(Exception):
    pass

alejos = [
    "nicolini",
    "alejo",
    "alejooo",
    "alejo nicolini",
    "alejo facha",
    "alejo gay",
]

while True:
    try:
        if personaje["nombre"].lower().strip() in alejos:
            raise Exception("sos autista")
    except Exception:
        print("Error: Mucho autismo detectado. No jugarás el juego. Adiós.")
        exit()

    print("")
    op = menu()
    if op == 1:
        print("")
        mostrar_personaje(personaje)
    elif op == 2:
        print("")
        op = menu_atacar(personaje)
    elif op == 3:
        print("")
        if personaje["pociones"] > 0:
            personaje["vida"] += 50
            if personaje["vida"] > personaje["vida_maxima"]:
                personaje["vida"] = personaje["vida_maxima"]
            personaje["pociones"] -= 1
            print("Te has curado 50 puntos de vida. Vida actual: ", personaje["vida"])
    elif op == 4:
        print("")
        op = tienda(personaje)
    elif op == 5:
        print("")
        break