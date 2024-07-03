#Clases y OBjetos Asociación

import random

class Laptop:

    #Método constructor

    def __init__(self,procesador, grafica, marca):

        #Atributos

        self.procesador = procesador
        self.grafica = grafica
        self.marca = marca

        #Método

    def encender(self):
        
        print("Ya prednio")

    def apagar(self):

        print("Ya se apago")

    def descripcion(self):

        print(f"laptop {self.marca}, gráfica {self.grafica} y procesador {self.procesador}")



#Asociación

class User:


    def __init__(self,name,laptop):

        self.name = name
        self.laptop = laptop

    def using(self):

        print(f"{self.name} esta usando la laptop {self.laptop.marca}")



laptop_1 = Laptop("I9","RTX 4090", "ASUS")

usuario_1 =User("Alejandro",laptop_1)

usuario_1.using()