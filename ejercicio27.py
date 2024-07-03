#Clases y Objetos Herencia


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



class Laptop_Repuesto(Laptop):

    def __init__(self,procesador, grafica, marca,area):

        super().__init__(procesador, grafica, marca)
        self.area = area

    def formatear(self):

        print(f"La laptop de repuesto de {self.area} se esta fomateando")


    def describir(self):

        super().describir()
        print (f"Laptop de serivico del area {self.area}")



laptop_repuesto_1 = Laptop_Repuesto("Ryzen Thread Reaper", "Titan RTX", "MSI","Administracion")

laptop_repuesto_1.describir()

