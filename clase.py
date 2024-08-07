

class Humano:

    def __init__(self, altura, peso, genero, ojos, nombre):

        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.ojos = ojos
        self.nombre = nombre

    def describir(self):

        
        print(f"Soy {self.genero} de {self.altura} con ojos de color {self.ojos}, peso {self.peso} kg y me llamo {self.nombre}")


persona_1 = Humano("1.7", "60 kg", "mujer", "ambar", "Blanca")

persona_1.describir()
        


