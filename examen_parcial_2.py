#Programa Completo


import random

class Laptop:

    #Método constructor

    def __init__(self,procesador, grafica, marca):

        #Atributos

        self.procesador = procesador
        self.grafica = grafica
        self.marca = marca
        self.jugar = None

        #Método

    def encender(self): 
        print("Ya prednio")

    def apagar(self):
        print("Ya se apago")


    def iniciar_juego(self,jugar):
        self.jugar = jugar


    def describir(self):
        print(f"laptop {self.marca}, gráfica {self.grafica} y procesador {self.procesador}")

        if self.jugar:

            print(f"Esta ejecutando {self.jugar}")


class Minar:

    def __init__ (self,crypto, tiempo, gains,laptop):

    #Atributos
        self.laptop = laptop
        self.crypto = crypto
        self.tiempo = tiempo
        self.gains = gains
        self.uso = random.randint(50,100)

    #Metodos
    def uso_grafica(self,laptop):
        print(f"el uso de la gráfica {laptop.grafica} es de {self.uso}%")


    def gains_hora (self):
        print(f"Estas generando {self.gains} {self.crypto} por hora")


    def total_gains(self):

        time = self.tiempo * self.gains

        print(f"Llevas minado {time} {self.crypto}")


class User:


    def __init__(self,name,laptop):

        self.name = name
        self.laptop = laptop
        self.usuarios = ["Alejandro"]

    def using(self):

        print(f"{self.name} esta usando la laptop {self.laptop.marca}")

    def lista(self):

        new = input("Nuevo usuario: ").title()

        self.usuarios.append(new)

        print(f"Lista de usuarios: {self.usuarios}")

        

class Juego:

    def __init__(self,jugar):

        #atrbutos

        self.jugar = jugar
    
    def describir(self):

        print(f"{self.juego} esta siendo ejecutado")


class Laptop_Repuesto(Laptop):

    def __init__(self,procesador, grafica, marca,area):

        super().__init__(procesador, grafica, marca)
        self.area = area

    def formatear(self):

        print(f"La laptop de repuesto de {self.area} se esta fomateando, puede pasar por ella")


    def describir(self):

        super().describir()
        print (f"Laptop de serivico para el area {self.area} esta disponible")


class Sistema:

    def __init__(self, os, laptop):

        self.os = os
        self. laptop = laptop

    def iniciar_os(self):

        print(f"iniciando {self.os} en {self.laptop.marca}")


class Rendimiento:

    def __init__(self,laptop,bateria):

        self.laptop = laptop
        self.bateria = bateria


    def maximo_rendimiento(self):

        print (f"{self.laptop.marca} esta en modo maximo rendimiento")
        print(f"bateria restante = {self.bateria}")

    def ahorro_energia(self):

        print(f"{self.laptop.marca} esta en modo ahorro de energía")
        print(f"bateria restante es = {self.bateria}")


class Procesador:

    def __init__(self, laptop):

        self.laptop = laptop
        self.frecuencia = random.randint(5,10)

    def overclock(self):

        while True:

            try:
                tiempo = float(input("Cuantas horas quieres que este activado? "))


            except ValueError:
                print("Expresa la cantidad en horas")



            if tiempo > 6:

                print(f"El procesador {self.laptop.procesador}, no resistirá el overclock por tanto tiempo")

            else:

                print(f"Overclock activado en {self.laptop.marca}")

                print(f"La laptop {self.laptop.marca} tiene un overclock del {self.frecuencia}%")

                break


    def estatus(self):

        print(f"el procesador {self.laptop.procesador} de {self.laptop.marca},tiene una frecuencia de {self.frecuencia} Ghz")



def menu():

    laptop_1 = Laptop("I9","RTX 4090", "ASUS")
    laptop_2 = Laptop("Ryzen 9", "Titan RTX", "MIS")
    laptop_repuesto_1 = Laptop_Repuesto("Ryzen Thread Reaper", "Titan RTX", "MSI","Administracion")



    print("________________________________________________________________________________________________")

    print("Bienvenido")
    print("________________________________________________________________________________________________")
    
    while True:

        print("Selecciona una accion")
        print("")
        print("(1): Crear Laptop,    (2): Minar,     (3): Usuario" )
        print("(4): Jugar,    (5): Respuestos,     (6): Sistema" )
        print("(7): Modo de energía,    (8): Procesador, (9):Salir")
        
        print("______________________________________________________________________________________________")

        opcion = int(input("Seleccion: "))

    

        match opcion:

            case 1:

                print("Creacion de una laptop")
                procesador = str(input("Procesador: "))
                grafica = str(input("Gráfica: "))
                marca = str(input("Marca: "))

                laptop_p = Laptop(procesador,grafica,marca)
                laptop_p.describir()
                laptop_p.encender()

                
            case 2:

                mina_1 = Minar("Bitcoin", 15, 0.1,laptop_1)
                mina_2 = Minar("Ethereum",50,0.3,laptop_2)

                print("(1): Ver uso de gráfica,     (2): Ver Ganancias por hora,    (3) Ver ganacias totales")

                opcion_2 = int(input("Seleccion: "))

                if opcion_2 == 1:

                    mina_1 = Minar("Bitcoin", 15, 0.1,laptop_1)
                    mina_2 = Minar("Ethereum",50,0.3,laptop_2)

                    mina_1.uso_grafica(laptop_1)
                    mina_2.uso_grafica(laptop_2)

                elif opcion_2 == 2:

                    mina_1.gains_hora()
                    mina_2.gains_hora()

                else:

                    mina_1.total_gains()
                    mina_2.total_gains()


            case 3:

                usuario_1 =User("Alejandro",laptop_1)

                print("(1): Ver usuarios activos,       (2) Agregar usuario: ")

                opcion_3 = int(input("Selecciona una opcion: "))

                if opcion_3 == 1:


                    usuario_1.using()

                else:
                    
                    usuario_1.lista()

            case 4:

                    juego_1 =Juego("Shadow of the Tomb Raider")


                    print("(1): Iniciar Juego")
                    opcion_4 = int(input("Selecciona: "))

                    if opcion_4 == 1:

                        laptop_1.iniciar_juego(juego_1.jugar)
                        laptop_1.describir()

            case 5:
                    
                    print("(1): Ver laptops de respuesto dispibles,     (2): Formatear la pc disponible")
                    opcion_5 = int(input("Selecciona: "))

                    if opcion_5 == 1:

                        laptop_repuesto_1.describir()

                    else:

                        laptop_repuesto_1.formatear()
                
            case 6:
                    
                    laptop_on = Sistema ("windows", laptop_1)
                    laptop_lin = Sistema ("Linux", laptop_2)


                    print("(1): Iniciar Winows,     (2): Iniciar Linux")

                    opcion_6 = int(input("Selecciona: "))

                    if opcion_6 == 1:

                        print(laptop_on.iniciar_os())

                   
                    else:

                        print(laptop_lin.iniciar_os())

            case 7:
                    modo_1 = Rendimiento(laptop_1,"95%")
                    modo_2 = Rendimiento(laptop_2,"88%")
                    
                    print("(1): Modo maximo Rendimiento,     (2): Ahorro de energía")

                    opcion_7 = int(input("Selecciona: "))

                    if opcion_7 == 1:

                        print("Maximo rendimiento para: Lap_1 (1), Lap (2):")
                        opcion_max = int(input("Selecciona: "))

                        if opcion_max == 1:

                            modo_1.maximo_rendimiento()
                        else:
                            modo_2.maximo_rendimiento()


                    else:

                        print("Ahorro de energía: Lap_1 (1), Lap (2):")
                        opcion_min = int(input("Selecciona: "))

                        if opcion_min == 1:

                            modo_1.ahorro_energia()
                        else:
                            modo_2.ahorro_energia()

            case 8:
                    procesador_1 = Procesador(laptop_1)
                    procesador_2 = Procesador(laptop_2)
                    
                    print("(1): Overclock,     (2): Estatus")

                    opcion_8 = int(input("Selecciona: "))

                    if opcion_8 == 1:

                        print("(1): Overclock a lap 1,     (2)Overclock a lap 2")

                        opcion_pro = int(input("Selecciona: "))

                        if opcion_pro == 1:

                            procesador_1.overclock()

                        else:

                            procesador_2.overclock()

                    else:

                        print("(1): Estatus lap 1,     (2)Estatus lap 2")

                        opcion_es = int(input("Selecciona: "))

                        if opcion_es== 1:

                            procesador_1.estatus()

                        else:

                            procesador_2.estatus()

            case _:

                print("__________________________________________________________________________________________")

                print("Gracias por haber consultado el sistema")

                print("__________________________________________________________________________________________")
                print(" /\_/\  ")
                print("( o.o ) ")
                print(" > ^ <  ")
                print("__________________________________________________________________________________________")
                break

menu()








  




                    



                    



                  


                    
        











                


