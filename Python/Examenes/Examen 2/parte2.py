def compara_poker(mano1,mano2):
    valores = "A23456789DJQK"
    palos = "ECDP"
    mano1 = mano1.split()
    valores_mano1 = dict()
    palos_mano1 = dict()
    puntos_mano1 = 0
    mano2 = mano2.split()
    valores_mano2 = dict()
    palos_mano2 = dict()
    puntos_mano2 = 0
    # --------- EXTRACCION DE DATOS MANO 1 ---------
    for x in mano1:
        if len(x) == 2:
            if x[0] in valores and x[1] in palos:
                if x[0] in valores_mano1.keys():
                    valores_mano1[x[0]] += 1
                else:
                    valores_mano1[x[0]] = 1
                
                if x[1] in palos_mano1.keys():
                    palos_mano1[x[1]] += str(x[0])
                else:
                    palos_mano1[x[1]] = str(x[0])

    # --------- EXTRACCION DE DATOS MANO 1 ---------
    # --------- EXTRACCION DE DATOS MANO 2 ---------
    for x in mano2:
        if len(x) == 2:
            if x[0] in valores and x[1] in palos:
                if x[0] in valores_mano2.keys():
                    valores_mano2[x[0]] += 1
                else:
                    valores_mano2[x[0]] = 1
                
                if x[1] in palos_mano2.keys():
                    palos_mano2[x[1]] += str(x[0])
                else:
                    palos_mano2[x[1]] = str(x[0])

    # --------- EXTRACCION DE DATOS MANO 2 ---------
    # --------- PUNTOS MANOS ---------
    puntos_mano1 = combinaciones(valores_mano1,palos_mano1)
    puntos_mano2 = combinaciones(valores_mano2,palos_mano2)
    if puntos_mano1 > puntos_mano2:
        return "GANADOR 1"
    elif puntos_mano2 > puntos_mano1:
        return "GANADOR 2"
    else:
        return "EMPATE"


    return puntos_mano1


def combinaciones(valores_carta,palos_carta):
    valores = "A23456789DJQK"
    palos = "ECDP"
    contador = 0
    # --------- COMBINACIONES MANO 1 ---------
        # --------- ESCALERA DE COLOR ---------
    if len(palos_carta) == 1:
        valores_carta_palo = list()
        for x in palos_carta.values():
            for l in x:
                valores_carta_palo.append(l)
        for v in valores_carta:
            if v in valores_carta_palo:
                posicion = valores.index(v)
                break
        while True:
            if contador == 5:
                return 8
            else:
                if valores_carta_palo[posicion] in valores_carta_palo:
                    posicion += 1
                    contador += 1
                else:
                    break
        # --------- ESCALERA DE COLOR ---------

        # --------- POKER ---------
    elif max(valores_carta.values()) == 4 and min(valores_carta.values()) == 1:
        for clave in valores_carta:
            if valores_carta[clave] == 4:
                return 7
        # --------- POKER ---------
        # --------- FULL ----------
    elif max(valores_carta.values()) == 3 and min(valores_carta.values()) == 2:
        punto_full = 0
        for clave in valores_carta:
            if valores_carta[clave] == 3 or valores_carta[clave] == 2:
                punto_full += 1
        if punto_full == 2:
            return 6
        # --------- FULL ----------
        # --------- COLOR ----------
    
    elif len(palos_carta) == 1:
        for x in palos_carta.keys():
            if len(palos_carta[x]) == 5:
                return 5
        # --------- COLOR ----------
        # --------- ESCALERA ----------
    
    elif len(valores_carta) == 5:
        values_valores_carta = list()
        for x in valores_carta.keys():
            for l in x:
                values_valores_carta.append(l)
        for v in valores:
            if v in values_valores_carta:
                posicion = valores.index(v)
                break
        while True:
            if contador == 5:
                return 4
            else:
                if valores[posicion] in values_valores_carta:
                    posicion += 1
                    contador += 1
                else:
                    break
        # --------- ESCALERA ----------
        # --------- TRIO ----------
    elif max(valores_carta.values()) == 3:
        if 3 in valores_carta.values():
            for clave in valores_carta:
                if valores_carta[clave] == 3:
                    return 3
        # --------- TRIO ----------
        # --------- DOBLE PAREJA ----------
    elif len(valores_carta) == 3:
        puntos_doble = 0
        for clave in valores_carta:
            if valores_carta[clave] == 2:
                puntos_doble += 1
        if puntos_doble == 2:
            return 2
        # --------- DOBLE PAREJA ----------
        # --------- PAREJA ----------
    elif len(valores_carta) == 4:
        for clave in valores_carta:
            if valores_carta[clave] == 2:
                return 1
        # --------- PAREJA ----------
    else:
        return 0