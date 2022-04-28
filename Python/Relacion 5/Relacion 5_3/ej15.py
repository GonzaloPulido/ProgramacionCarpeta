def dato_en_agenda(dato,agenda):
    if es_nombre(dato):
        if dato in agenda.keys():
            return True
        else:
            return False
    elif es_numero(dato):
        if dato in agenda.values():
            return True
        else:
            return False
    return None

def dar_nombre(numero,agenda):
    for clave,valor in agenda.items():
        if valor == numero:
            return clave
    

def es_nombre(entrada):
    if entrada[0].isalpha():
        return True
    return False

def es_numero(entrada): # +34 691 27 08 67
    # Internacional
    if entrada[0] == "+" and len(entrada.split())> 1:
        new_entrada = entrada.replace(" ","")
        if new_entrada[1:-1].isnumeric():
            lista_split = entrada.split()
            if len(lista_split[0]) > 1 and len(lista_split[0]) <= 5:
                return True
    # España
    entrada = entrada.replace(" ","")

    if entrada.isnumeric() and len(entrada) == 9:
        return True
    # No valido
    return None

def filtra_x(dato,agenda):
    diccionario = dict()
    lista = list()
    for clave in agenda.keys():
        if dato in clave:
            diccionario = {clave : agenda[clave]}
            lista.append(diccionario)
    return lista

            


if __name__=="__main__":
    agenda_telefonica = dict()
    while True:
        entrada = input('Introduce un numero de telefono un nombre o un comando: ')
        if entrada.lower() == 'adios':
            break
        elif entrada.lower() == 'listado':
            if len(agenda_telefonica) < 1:
                print("Aun no hay datos existentes")
            else:
                agenda_ordenada = sorted(agenda_telefonica.items())
                print(agenda_ordenada)
        elif entrada.lower()[0:6] == 'filtra':
            entrada = entrada.split()
            if len(filtra_x(entrada[1], agenda_telefonica)) >= 1:
                print(filtra_x(entrada[1], agenda_telefonica))
            else:
                print("Ningun contacto")
        elif es_nombre(entrada):
            if dato_en_agenda(entrada,agenda_telefonica):
                print("El numero de telefono de",entrada,'es',agenda_telefonica[entrada])
            elif not dato_en_agenda(entrada,agenda_telefonica):
                numero_telefono = input(f'Introduce el numero de telefono para {entrada}: ')
                if es_numero(numero_telefono):
                    if dato_en_agenda(numero_telefono,agenda_telefonica):
                        print('Ese numero ya existe en la agenda')
                    elif not dato_en_agenda(numero_telefono,agenda_telefonica):
                        agenda_telefonica[entrada] = numero_telefono
                else:
                    print('Numero de telefono no valido')
            
        elif es_numero(entrada):
            if dato_en_agenda(entrada,agenda_telefonica):
                print("El nombre dado al telefono",entrada,'es',dar_nombre(entrada,agenda_telefonica))
            elif not dato_en_agenda(entrada,agenda_telefonica):
                nombre_telefono = input(f'Introduce el nombre para el numero {entrada}:')
                if es_nombre(nombre_telefono):
                    if dato_en_agenda(nombre_telefono,agenda_telefonica):
                        print('Ese numero ya existe en la agenda')
                    elif not dato_en_agenda(nombre_telefono,agenda_telefonica):
                        agenda_telefonica[nombre_telefono] = entrada
                else:
                    print('Numero de telefono no valido')
            
        else:
            print("Entrada no valida")