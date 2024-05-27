import math



while True:

    print("Circulo: 1, Triangulo: 2, rectángulo: 3, 4 para salir")
    calculo = int((input("De qué figura quieres clacular el area? ")))


    if calculo == 1:

        radio = float(input("Ingrese el radio: "))

        area = math.pi * radio**2

        print(f"El area del circulo es {area}")

    elif calculo == 2:

        base = float(input("Ingrese la base: "))

        altura = float(input("Ingrese altura: "))

        area = base* altura/2

        print(f"El area del trienagulo es : {area}")

    elif calculo == 3:

        b = float(input("Ingrese la base: "))

        a = float(input("Ingrese al altura: "))

        area = a*b

        print(f"El area del rectángulo es {area}")

    else:
        break

