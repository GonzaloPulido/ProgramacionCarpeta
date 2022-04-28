from ej21 import comprobar_fecha

def dia_semana(day,month,year,dia_enero):
    pass

if __name__=="__main__":
    dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    while True:
        try:
            day = int(input("Introduce el dia de la fecha: "))
            month = int(input("Introduce el mes de la fecha: "))
            year = int(input("Introduce el año de la fecha: "))
            dia_enero = input("Introduce el dia que fue el 1 de enero de el año introducido: ")
            if comprobar_fecha(day,month,year) and dia_enero.lower() in dias:
                break
            else:
                print("Los datos introducidos no son correctos")
        except ValueError:
            print("Los datos deben ser numeros")