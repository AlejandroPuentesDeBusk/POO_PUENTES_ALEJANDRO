class Perro:

    def __init__(self,nombre,raza,edad):
        #Atributos
        self.nombre= nombre 
        self.raza = raza
        self.edad = edad

    #Métodos
    def ladrar(self):

        print("Guau")

    def comer(self):

        print("COmiendo... ")

#Objetos

perro1 = Perro("Firulais","Golden",15)
perro2 = Perro("Solovino","Husky",10)

#Usaros

print(perro1.nombre)
print(perro2.nombre, perro2.raza)

perro1.ladrar()
perro2.comer()