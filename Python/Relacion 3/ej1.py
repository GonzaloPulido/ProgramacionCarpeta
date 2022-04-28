def area_triangulo(base,altura):
    return base*altura/2

if __name__=="__main__":
    while True:
        try:
            base = float(input("Introduce la base del triangulo: "))
            altura = float(input("Introduce la altura del triangulo: "))
            if base <= 0 or altura <= 0:
                print("La base y la altura deben ser mayor que 0")
            else:
                break
        except ValueError:
            print("Eso no es un numero")

    print("El area del triangulo es",area_triangulo(base,altura))