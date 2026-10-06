from funciones.entidades import *
from funciones.func import *
import random
import os

def menu():
    while True:
        try:
            op = int(input("Elija una opcion (1 ver personaje), (2 atacar enemigo), (3 curar), (4 comprar), (5 salir) "))
        except ValueError:
            print("Error, elige una opción válida")
            continue
        return op



def tienda(personaje: dict):
    print("""
    1)Daga $1150
    2)Espada $1200
    3)Arco $1500

    4)Casco $2700
    5)Pechera $3500

    6)Pocion $500
    """)
    opTienda = int(input("Elija una opcion (1-6) "))
    print("Monedas actuales: ", personaje["monedas"])

    if opTienda == 1 and personaje["monedas"] >= armas["daga"]["precio"]:
        personaje["monedas"] -= armas["daga"]["precio"]
        personaje["arma"] = "daga"
        personaje["fuerza"] = personaje["fuerza_base"] + armas["daga"]["daño"]
    elif opTienda == 2 and personaje["monedas"] >= armas["espada"]["precio"]:
        personaje["monedas"] -= armas["espada"]["precio"]
        personaje["arma"] = "espada"
        personaje["fuerza"] = personaje["fuerza_base"] + armas["espada"]["daño"]
    elif opTienda == 3 and personaje["monedas"] >= armas["arco"]["precio"]:
        personaje["monedas"] -= armas["arco"]["precio"]
        personaje["arma"] = armas["arco"]
        personaje["fuerza"] = personaje["fuerza_base"] + armas["arco"]["daño"]
    elif opTienda == 4 and personaje["monedas"] >= armaduras["casco"]["precio"]:
        personaje["monedas"] -= armaduras["casco"]["precio"]
        personaje["armadura"] = "casco"
        personaje["vida_maxima"] += armaduras["casco"]["resistencia"]
    elif opTienda == 5 and personaje["monedas"] >= armaduras["pechera"]["precio"]:
        personaje["monedas"] -= armaduras["pechera"]["precio"]
        personaje["armadura"] = "pechera"
        personaje["vida_maxima"] += armaduras["pechera"]["resistencia"]
    elif opTienda == 6 and personaje["monedas"] >= 500:
        personaje["monedas"] -= 500
        personaje["pociones"] += 1
    else: print("No tienes suficientes monedas o la opcion no es valida.")
    print("")
    return True

def menu_atacar(personaje: dict):
    atac=input("Elija el modo de combate (1 individual), (2 torre) ")
    if atac == "1":
        enemigo = elegir_enemigo().copy()
        atac, personaje = iniciar_ataque(personaje, enemigo)
    elif atac == "2":
        torre = []
        for i in range(random.randint(3, 10)):
            enemigo = elegir_enemigo().copy()
            torre.append(enemigo)
        atac, personaje = iniciar_torre(personaje, torre)
    else: print("Opcion no valida, elija 1 o 2")

def iniciar_ataque(personaje, enemigo):
    print("PELEA INICIADA CONTRA ", enemigo["nombre"])
    while True:
        #Ataque pj
        print("ATACAS TU")
        opcion = int(input("Elija una opcion (1 atacar), (2 usar pocion) "))
        if opcion == 1:
            if random.randint(1, 100) <= personaje["suerte"]:
                ataque = personaje["fuerza"] + personaje["fuerza"] * (personaje["suerte"] / 100)
                print("¡Golpe crítico!")
            else:
                ataque = personaje["fuerza"]

                
            enemigo["vida"] -= ataque
            if enemigo["vida"] <= 0:
                print("¡Has derrotado a ", enemigo["nombre"], "!")
                personaje["monedas"] += enemigo["tesoro"]
                print("Has ganado ", enemigo["tesoro"], " monedas. monedas actual: ", personaje["monedas"])
                break
        else:
            if personaje["pociones"] > 0:
                personaje["vida"] += 50
                if personaje["vida"] > personaje["vida_maxima"]:
                    personaje["vida"] = personaje["vida_maxima"]
                personaje["pociones"] -= 1
                print("Has usado una pocion. Vida actual: ", personaje["vida"])
            else:
                print("No tienes pociones disponibles.")
                continue
        print("Vida del enemigo: ", enemigo["vida"])
        print("")
        #Ataque enemigo
        print("ATACA ", enemigo["nombre"])
        if random.randint(1, 100) <= enemigo["tesoro"] / 100:
            ataque = enemigo["daño"] * 2
            print("¡Golpe crítico!")
        else:
            ataque = enemigo["daño"]
        personaje["vida"] -= ataque
        print("Te han atacado. Vida actual: ", personaje["vida"])
        print("")
        if personaje["vida"] <= 0:
            print("¡Has sido derrotado por ", enemigo["nombre"], "!")
            exit()
    return True, personaje

def iniciar_torre(personaje, torre):
    print("TORRE INICIADA, ENEMIGOS: ", len(torre))
    print("")
    for i in range(len(torre)-1, -1, -1):
        enemigo = torre.pop(i)
        print("PELEA INICIADA CONTRA ", enemigo["nombre"])
        while True:
        #Ataque pj
            print("ATACAS TU")
            opcion = int(input("Elija una opcion (1 atacar), (2 usar pocion) "))
            if opcion == 1:
                if random.randint(1, 100) <= personaje["suerte"]:
                    ataque = personaje["fuerza"] + personaje["fuerza"] * (personaje["suerte"] / 100)
                    print("¡Golpe crítico!")
                else:
                    ataque = personaje["fuerza"]

                    
                enemigo["vida"] -= ataque
                if enemigo["vida"] <= 0:
                    print("¡Has derrotado a ", enemigo["nombre"], "!")
                    personaje["monedas"] += enemigo["tesoro"]
                    print("Has ganado ", enemigo["tesoro"], " monedas. monedas actual: ", personaje["monedas"])
                    break
            else:
                if personaje["pociones"] > 0:
                    personaje["vida"] += 50
                    if personaje["vida"] > personaje["vida_maxima"]:
                        personaje["vida"] = personaje["vida_maxima"]
                    personaje["pociones"] -= 1
                    print("Has usado una pocion. Vida actual: ", personaje["vida"])
                else:
                    print("No tienes pociones disponibles.")
                    continue
            print("Vida del enemigo: ", enemigo["vida"])
            print("")
            #Ataque enemigo
            print("ATACA ", enemigo["nombre"])
            if random.randint(1, 100) <= enemigo["tesoro"] / 100:
                ataque = enemigo["daño"] * 2
                print("¡Golpe crítico!")
            else:
                ataque = enemigo["daño"]
            personaje["vida"] -= ataque
            print("Te han atacado. Vida actual: ", personaje["vida"])
            print("")
            if personaje["vida"] <= 0:
                print("¡Has sido derrotado por ", enemigo["nombre"], "!")
                exit()
    return True, personaje
