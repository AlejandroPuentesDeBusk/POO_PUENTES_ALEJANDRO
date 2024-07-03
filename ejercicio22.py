
def suma():

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    print(f"La suma es = {n1+n2}")

def resta():

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    print(f"La resta es = {n1-n2}")

def multi():

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    print(f"La multiplicacion es = {n1*n2}")

def div():

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    print(f"La division es = {n1/n2}")


while True:
    try:

        print("suma(1), resta(2), multiplicacion(3), division (4), salir(5)")
        operacion = int(input("Seleccione la opración"))

        match operacion:

            case (operacion) if operacion == 1:

                suma()

            case (operacion) if operacion == 2:

                resta()

            case (operacion) if operacion == 3:

                multi()

            case (operacion) if operacion == 4:

                div()

            case (operacion) if operacion == 5:

                break


    except ValueError:

        print("seleccione un valor correcto")



