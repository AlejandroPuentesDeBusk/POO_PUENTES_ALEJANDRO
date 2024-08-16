

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


laptop_1 = Laptop("Intel Xeon", "RTX 2080 TI", "MSI")

laptop_2 = Laptop("AMD RYZEN 9 7950XT", "AMD RADEON 7900 XTX", "RAZER")


laptop_1.encender()
laptop_1.descripcion()

laptop_2.descripcion()
















