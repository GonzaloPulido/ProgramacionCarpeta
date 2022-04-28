def division_con_restas(dividendo,divisor):
    contador = 0
    while dividendo >= divisor:
        dividendo -= divisor
        contador +=1
    return contador,dividendo

if __name__=="__main__":
    while True:
        try:
            dividendo = int(input("Introduce el dividendo de la division: "))
            divisor = int(input("Introduce el divisor de la division: "))
            if divisor == 0:
                print("No se puede dividir entre 0")
            else:
                break
        except ValueError:
            print("Eso no es un numero")

    print("El cociente y el resto de la division son",division_con_restas(dividendo,divisor))