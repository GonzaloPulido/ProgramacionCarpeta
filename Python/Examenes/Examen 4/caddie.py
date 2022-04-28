def comprobar_hoyo(hoyo,lista):
    for x in lista:
        if x["HOYO"] == hoyo:
            return True
    return False

def modificar_par(hoyo,par,lista):
    for x in lista:
        if x["HOYO"] == hoyo:
            x["PAR"] = par
            return x 
    

def hay_golpes(hoyo,lista):
    for x in lista:
        if x["HOYO"] == hoyo:
            if "GOLPES" in x.keys():
                return True
    return False

def añadir_modificar_golpes(hoyo,golpes,lista):
    for x in lista:
        if x["HOYO"] == hoyo:
            x["GOLPES"] = golpes
            return x
    
def termino_golf(hoyo,lista):
    for x in lista:
        if x["HOYO"] == hoyo:
            par = x["PAR"]
            golpes = x["GOLPES"]
            if par == golpes:
                return "PAR"
            elif par - golpes == 1:
                return "BIRDIE"
            elif golpes -par == 1:
                return "BOGEY"
            elif par - golpes == 2:
                return "EAGLE"
            elif golpes - par == 2:
                return "DOBLE BOGEY"
            else:
                return "FUERA DE RANGO"

def devolver_listado(lista):
    lista_ordenada = []
    contador = 1
    while contador <= 18:
        for x in lista:
            if x["HOYO"] == contador:
                lista_ordenada.append(x)
        contador += 1 
    return lista_ordenada 

def resultado(lista):
    lista_resultado = []
    for x in lista:
        if "GOLPES" in x.keys():
            if x["PAR"] > x["GOLPES"]:
                diferencia = x["PAR"] - x["GOLPES"]
                diccionario =  {"HOYO":x["HOYO"],"DIFERENCIA":diferencia}
                lista_resultado.append(diccionario)
            elif x["GOLPES"] > x["PAR"]:
                diferencia =  x["GOLPES"] - x["PAR"]
                diccionario =  {"HOYO":x["HOYO"],"DIFERENCIA":diferencia}
                lista_resultado.append(diccionario)
            else:
                diferencia = 0
                diccionario =  {"HOYO":x["HOYO"],"DIFERENCIA":diferencia}
                lista_resultado.append(diccionario)

    return lista_resultado
           
if __name__=="__main__":
    # golf = [{"HOYO":1,"PAR":4,"GOLPES":7},{"HOYO":3,"PAR":4,"GOLPES":7}]
    golf = []
    while True:
        entrada = input("Introduce la accion en este programa de golf: ")
        # --------- HOYO/PAR ---------
        if entrada.split()[0] == "par":
            if entrada.split()[1].isnumeric() and entrada.split()[2].isnumeric():
                hoyo = int(entrada.split()[1])
                par = int(entrada.split()[2])
                if hoyo >=1 and hoyo <= 18 and par >= 1:
                    if comprobar_hoyo(hoyo,golf):
                        modificar = input("Ese hoyo ya existe, ¿desea modificar su par? Y/N:")
                        if modificar == "Y":
                            modificar_par(hoyo,par,golf)
                        else:
                            continue
                    else:
                        diccionario = {"HOYO":hoyo,"PAR":par}
                        golf.append(diccionario)
            else:
                print("¡VAYA! Parece que uno de los datos no es valido")
        # --------- HOYO/GOLPES ---------
        elif len(entrada.split()) == 2:
            if entrada.split()[0].isnumeric() and entrada.split()[1].isnumeric():
                hoyo = int(entrada.split()[0])
                golpes = int(entrada.split()[1])
                if hoyo >=1 and hoyo <= 18:
                    if comprobar_hoyo(hoyo,golf):    # {"HOYO":1,"PAR":4,"GOLPES":8}
                        if hay_golpes(hoyo,golf):
                            entrada = input("Ese hoyo ya tiene golpes, ¿desea modificarlo? Y/N")
                            if entrada == "Y":
                                añadir_modificar_golpes(hoyo,golpes,golf)
                                print(termino_golf(hoyo,golf))
                            else:
                                continue
                        else:
                            añadir_modificar_golpes(hoyo,golpes,golf)
                            print(termino_golf(hoyo,golf))

                            
                    else:
                        par = input("Ese hoyo, no existe aun, introduzca un par para ese hoyo: ")
                        if par.isnumeric():
                            par = int(par)
                            if par >= 1:
                                diccionario = {"HOYO":hoyo,"PAR":par,"GOLPES":golpes}
                                golf.append(diccionario)
                                print(termino_golf(hoyo,golf))
                        else:
                            print("Par no valido")
                else:
                    print("Hoyo no valido")
        elif entrada == "listado":
            if len(golf) >= 2:
                print(devolver_listado(golf))
            else:
                print("Debe haber 2 hoyos o mas para mostrarlos ordenados")
        elif entrada == "resultado":
            print(resultado(golf))
        else:
            print("Entrada no valida")