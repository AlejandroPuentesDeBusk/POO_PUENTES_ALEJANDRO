def temp():

    x = True

    while x == True:

       

        print("Conversion de celsius a fahrenheit, presione 1")
        print("Conversion de fahrenheit a celsius , presione 2")
        print("Para salir presione 3")

        select = int(input())

        if select == 1:

            tem = float(input("Ingrese temperatura en celcius: "))

            print(f"La cantidad en cilcius es = {(tem *9/5)+32}")

        elif select == 2:

            tem = float(input("Ingrese temperatura en fahrenheit: "))

            print(f"La cantidad en fahrenheit es = {(tem -32)*5/9}")

        elif select == 3:
            break
    

temp()



