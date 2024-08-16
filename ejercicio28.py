#Dependencia


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


class Sistema:

    def __init__(self, os, laptop):

        self.os = os
        self. laptop = laptop

    def iniciar_os(self):

        print(f"iniciando {self.os} en {self.laptop.marca}")



laptop_1 = Laptop("I9","RTX 4090", "ASUS")

laptop_on = Sistema ("windows", laptop_1)

print(laptop_on.iniciar_os())