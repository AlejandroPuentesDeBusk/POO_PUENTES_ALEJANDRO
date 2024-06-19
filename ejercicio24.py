class Laptop:

    #Método constructor

    def __init__(self,procesador, grafica, marca):

        #Atributos

        self.procesador = procesador
        self.grafica = grafica
        self.marca = marca

        #Método

    def encender():
        
        print("Ya prednio")

    def apagar():

        print("Ya se apago")

    def minar():

        print("Minando bitcoin")

#Objetos

laptop_1 = Laptop("I9","RTX 4090", "ASUS")
laptop_2 = Laptop("Ryzen 9", "Titan RTX", "MIS")

#Uso

print(laptop_1.encender, laptop_1.minar)

print(laptop_2.encender)





