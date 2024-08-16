lista = [6,7,8,12,13,14,15,18,19,40,50]


while True:

    try: 

        print("Infancia: 1, Adoleascentes: 2, Jovenes: 3, Adultos: 4, 5 para salir")

        buscar = int(input("Que lista quieres ver? "))


        if buscar == 1:

            for i in lista:

                if i >=6 and i <= 11:

                    infancia_lista=[i]
                    print(infancia_lista)

        elif buscar == 2:
                
                for i in lista:
                
                    if i >= 12 and i <= 17:

                        ado_lista=[i]
                        print(ado_lista)

        elif buscar == 3:
                
                for i in lista:
                
                    if i >= 18 and i <= 26:

                        jovenes_lista=[i]
                        print(jovenes_lista)

        elif buscar == 4:
                
                for i in lista:
                
                    if i > 26:

                        adultos_lista=[i]
                        print(adultos_lista)
                    
        else:
            break

    except ValueError:
         
         print("Ingresa un valor del menu")




