def main():

    while True:

        try:


            n = float(input("Ingrese un numero: "))

            if n < 0:

                print("El numero ingresado es negativo")
                break

            elif n > 0:

                print("El numero es positivo")
                break

            else:

                print("El numero es 0")
                break

        except ValueError:

            print("Ese no es un numero")


main()

    