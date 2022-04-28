import random
from parte1 import filtra_ejercicios,entrenamiento
from ejercicios import ejercicios

def crear_diccionario(denominacion,descripcion,duracion,estrategia,ejercicios):
    diccionario = {"denominacion":denominacion,"descripcion":descripcion,"duracion":duracion,"estrategia":estrategia}
    ejercicios.append(diccionario)
    

if __name__=="__main__":
    def imprimir_diccionario(diccionario):
        denominacion = diccionario["denominacion"]
        descripcion = diccionario["descripcion"]
        duracion = diccionario["duracion"]
        estrategia = diccionario["estrategia"]
        print(denominacion,"(",duracion,")\n",descripcion,"\nEstrategia: ")
        for x in estrategia:
            print("\t-",x)

    while True:
        entada = input("Introduce la accion que desees: ")
        if entada == "crear":
            print("Por lo que veo, quieres crear un entrenamiento")
            denominacion = input("Facilitame la denominacion: ")
            descripcion = input("Facilitame la descripcion: ")
            duracion = input("Facilitame la duracion, debe ser un numero multiplo de 10: ")
            print("A continuacion debes facilitar todas las estrategias que necesites, si quieres dejar de introducir estrategias introduce fin")
            lista_estrategia = []
            while True:
                estrategia = input("Facilitame la denominacion: ")
                if estrategia == "fin":
                    if len(lista_estrategia) >= 1:
                        break
                    else:
                        print("Debes introducir almenos una estrategia")
                else:
                    lista_estrategia.append(estrategia)
            if duracion.isnumeric():
                duracion = int(duracion)
                if duracion % 10 == 0:
                    crear_diccionario(denominacion,descripcion,duracion,lista_estrategia,ejercicios)

        elif entada== "listado":
            for x in ejercicios:
                imprimir_diccionario(x)


        elif entada.split()[0] == "entrenamiento":
            if entada.split()[1].isnumeric():
                duracion = int(entada.split()[1])
                print(entrenamiento(ejercicios,duracion))
            else:
                print("Dato no valido")

        elif entada.split()[0] == "consulta":
            if entada.split()[1].isnumeric():
                duracion = int(entada.split()[1])
                if duracion % 10 == 0:
                    print(filtra_ejercicios(ejercicios,duracion))
            else:
                print("Dato no valido")

        elif entada == "fin":
            break