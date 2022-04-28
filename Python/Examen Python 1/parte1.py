from ejercicios import ejercicios
import random

def filtra_ejercicios(lista,minutos):
    lista_resultado = []
    for x in lista:
        if x["duracion"] <= minutos:
            lista_resultado.append(x)

    return lista_resultado

def duracion_ejercicios(lista):
    duracion = 0
    for x in lista:
        duracion += x["duracion"]

    return duracion

def entrenamiento(lista,minutos):
    contador_minutos = 0
    lista_resultado = []
    while True:
        valor = random.choice(lista)
        if contador_minutos > minutos:
            contador_minutos = 0
            lista_resultado = []
        elif contador_minutos == minutos:
            break
        elif not valor in lista_resultado:
            contador_minutos += valor["duracion"] 
            lista_resultado.append(valor)
        
    return lista_resultado