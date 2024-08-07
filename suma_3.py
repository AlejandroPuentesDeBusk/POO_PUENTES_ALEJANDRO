import sys


def main():

    numero = suma()
    print(numero)

def suma():

    triple = []

    try:
        for i in range(3):
            a = float(input("Dame un numero: "))
            triple.append(a)


    except ValueError:
        print("Ese no es un numero")

    result = triple[0] + triple[1] + triple[2]

    return result


if __name__ == "__main__":
    main()