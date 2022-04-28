from juego1 import jugador,aplica

def crear_diccionario(nombre,pv):
    diccionario = {"NOMBRE":nombre,"PV":pv}
    return diccionario

def crear_ataque(jugador,objetivo,pv,posibilidad):
    diccionario = {"JUGADOR":jugador,"OBJETIVO":objetivo,"PV":pv,"POSIBILIDAD":posibilidad,"TIPO":"Atacar"}
    return diccionario

def crear_cura(jugador,pv):
    diccionario = {"JUGADOR":jugador,"PV":pv,"TIPO":"Curar"}
    return diccionario

def comprobar_nombre(nombre,lista):
    for diccionario in lista:
        if nombre in diccionario.values():
            return diccionario
    return False



if __name__=="__main__":
    lista_jugadores = list()
    while True:
        entrada = input("Introduce los datos: ")
        if entrada.split()[0] == "crear" and len(entrada.split()) == 3:
            entrada_mod = entrada.split()
            if entrada_mod[1][0].isalpha() and entrada_mod[2].isnumeric():
                diccionario = crear_diccionario(entrada_mod[1],int(entrada_mod[2]))
                lista_jugadores.append(diccionario)
            else:
                print("Alguno de los datos no es valido")
        elif entrada.split()[0] == "ataque" and len(entrada.split()) == 5:
            entrada_mod = entrada.split()
            if entrada_mod[1][0].isalpha() and entrada_mod[2][0].isalpha() and entrada_mod[3].isnumeric() and entrada_mod[3].isnumeric():
                if comprobar_nombre(entrada_mod[1],lista_jugadores):
                    ataque = crear_ataque(entrada_mod[1],entrada_mod[2],int(entrada_mod[3]),int(entrada_mod[4]))
                    jugador = comprobar_nombre(entrada_mod[1],lista_jugadores)
                    aplica(jugador,ataque)
                else:
                    print("Alguno de los datos no es valido")
        elif entrada.split()[0] == "cura" and len(entrada.split()) == 3:
            entrada_mod = entrada.split()
            if entrada_mod[1][0].isalpha() and entrada_mod[2].isnumeric():
                if comprobar_nombre(entrada_mod[1],lista_jugadores):
                    jugador = comprobar_nombre(entrada_mod[1],lista_jugadores)
                    cura = crear_cura(entrada_mod[1],int(entrada_mod[2]))
                    aplica(jugador,cura)
                    print(lista_jugadores)
        elif entrada == "listado":
            print(lista_jugadores)
        elif entrada == "fin":
            break
        else:
            print("Entrada no valida")