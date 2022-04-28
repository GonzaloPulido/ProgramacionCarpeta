while True:
    try:
        celsius = float(input("Introduce tus grados en celsius: "))
        break
    except ValueError:
        print("La temperatura tiene que ser introducida con numeros")

fahrenheit = celsius * 9 / 5 + 32

print(celsius,"grados Celsius son",fahrenheit,"grados Fahrenheit")