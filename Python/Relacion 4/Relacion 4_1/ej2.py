from ej1 import lista_numeros


if __name__=="__main__":
    lista_num = []
    contador = 0
    while True:
        try:
            entrada = input("Introduce numeros o bien introduce fin para salir del programa: ")
            if entrada == "fin" and contador > 0:
                break
            elif entrada =="fin" and contador == 0:
                print("Recuerda que tienes que introducir almenos un numero para salir")
            entrada = int(entrada)
            lista_num.append(entrada)
            contador += 1

        except ValueError:
            print("Incorrecto")
            
    print("La suma, la cantidad y la media son",lista_numeros(lista_num))