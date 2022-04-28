import random

def jugador(lista,nombre):
    for x in lista:
        if nombre in x.values():
            return x

def aplica(player,accion):
    if accion["TIPO"] == "Atacar":
        numero = random.randint(1,100)
        puntos_ataque = accion["PV"] 
        if numero >= 1 and numero <= accion["POSIBILIDAD"]:
            player["PV"] -= puntos_ataque
        return player

    elif accion["TIPO"] == "Curar":
        vida_jugador = player["PV"]
        puntos_cura = accion["PV"] 
        player["PV"] += puntos_cura
        return player