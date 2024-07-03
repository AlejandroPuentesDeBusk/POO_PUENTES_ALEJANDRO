#Clases y Objetos Composición


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


class Juego:

    def __init__(self,jugar):

        #atrbutos

        self.jugar = jugar
    
    def describir(self):

        print(f"{self.juego} esta siendo ejecutado")


laptop_1 = Laptop("I9","RTX 4090", "ASUS")

juego_1 =Juego("Shadow of the Tomb Raider")

laptop_1.iniciar_juego(juego_1.jugar)

laptop_1.describir()