import random

vida_maxima= 100

personaje_principal = {
    "nombre" : "",
    "vida_maxima" : vida_maxima,
    "vida" : vida_maxima,
    "fuerza" : 0,
    "suerte" : 0,
    "monedas" : 0,
    "pociones" : 1,
    "arma" : {},
    "armadura" : {},
    "fuerza_base": 0 
}

armas = {
    "puño" : {
            "daño" : personaje_principal["fuerza"],
            "precio" : 0
            },
    "espada" : {
        "daño" : 10,
        "precio" : 1200
        },
    "arco" : {
        "daño" : 7,
        "precio" : 1500
        },
    "daga" : {
        "daño" : 5,
        "precio" : 1150
    }
}

armaduras = {
    "casco" : {
        "resistencia" : 100,
        "precio" : 2700
    },
    "pechera" : {
        "resistencia" : 100,
        "precio" : 3500
    }
}

enemigos = {
    "arquero": {
        "nombre" : "Arquero",
        "vida" : 200,
        "daño" : 30,
        "tesoro" : 1500
    },
    "zombie" : {
        "nombre" : "Zombie",
        "vida" : 260,
        "daño" : 20,
        "tesoro" : 2000
    },
    "slime" : {
        "nombre" : "Slime",
        "vida" : 100,
        "daño" : 15,
        "tesoro" : 500
    }
}

def generar_personaje(nombre):
    global personaje_principal

    personaje = personaje_principal.copy()

    personaje["nombre"] = nombre
    personaje["fuerza"] = random.randint(20, 100)
    personaje["fuerza_base"] = personaje["fuerza"]
    personaje["suerte"] = random.randint(1, 100)

    if personaje["nombre"] == "LIONEL MESSI":
        personaje["fuerza"] = 150
        personaje["suerte"] = 100
        personaje["monedas"] = 10000

    mostrar_personaje(personaje)

    return personaje

def mostrar_personaje(personaje: dict):
    print("Nombre: ", personaje["nombre"])
    print("vida: ", personaje["vida"], "/", personaje["vida_maxima"])
    print("fuerza: ", personaje["fuerza"], " suerte: ", personaje["suerte"])
    print("monedas: $", personaje["monedas"])
    print("cantidad de pociones: ", personaje["pociones"])

    if personaje["arma"] != {}:
        print("arma: ", personaje["arma"])
    if personaje["armadura"] != {}:
        print("armadura: ", personaje["armadura"])

def mostrar_enemigo(enemigos: dict):
    print("nombre: ", enemigos["nombre"])
    print("vida: ", enemigos["vida"])
    print("daño: ", enemigos["daño"])
    print("tesoro: $", enemigos["tesoro"])

def elegir_enemigo():
    global enemigos
    num=random.randint(1,3)
    if num == 1:
        return enemigos["arquero"]
    elif num == 2:
        return enemigos["zombie"]
    else:
        return enemigos["slime"]