#Clases y objetos Agregación

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


#Objetos

laptop_1 = Laptop("I9","RTX 4090", "ASUS")
laptop_2 = Laptop("Ryzen 9", "Titan RTX", "MIS")


mina_1 = Minar("Bitcoin", 15, 0.1,laptop_1)
mina_2 = Minar("Ethereum",50,0.3,laptop_2)


#Uso

laptop_1.descripcion()
mina_1.gains_hora()
mina_1.total_gains()
mina_1.uso_grafica(laptop_1)