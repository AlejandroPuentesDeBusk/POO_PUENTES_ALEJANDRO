def prom():

    while True:

        try:

            average1 = float(input(f"promedio= "))
            average2 = float(input(f"promedio= "))
            average3 = float(input(f"promedio= "))

            if average1 > average2 and average1 > average3:

                print(f"El primedio mayor es el primero {average1}")

            elif average2 > average1 and average2 > average3:

                print(f"El promedio mayor es el segundo {average2}")

            else:

                print(f"El promedio mayor es el tercero {average3}")

            break

        except ValueError:

            print("Ese no es un promedio")

prom()



            
