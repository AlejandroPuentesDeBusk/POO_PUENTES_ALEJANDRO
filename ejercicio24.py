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

    def jugar():

        print("Jugando MINECRAFT")


class Minar:

    def __init__ (self,crypto, tiempo, gains,laptop):

    #Atributos
        self.laptop = laptop
        self.crypto = crypto
        self.tiempo = tiempo
        self.laptops = []
        self.gains = gains

    #Metodos
    def minando(self,laptop):

        self.laptops.append(laptop)
        print(f"Estan minando {self.laptop.marca}, {self.crypto}")


    def gains_hora (self):

        print(f"Estas generando {self.gains}, por hora")

    def total_gains(self):

        time = self.tiempo * self.gains

        print(f"Llevas minado {time} {self.crypto}")


        




#Objetos

laptop_1 = Laptop("I9","RTX 4090", "ASUS")
laptop_2 = Laptop("Ryzen 9", "Titan RTX", "MIS")


mina_1 = Minar("Bitcoin", 10, 0.1,laptop_1)
mina_2 = Minar("Ethereum",50,0.3,laptop_2)





#Uso



#print(laptop_1.encender, laptop_1.jugar)

#print(laptop_2.encender)





