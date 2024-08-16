#Clases y Objetos

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
        

    def describir(self):

        print("Soy un perro llamado", self.nombre, "soy raza", self.raza, "y tengo", self.edad, "años")


class Dueño:

    def __init__(self,nombre):

        self.nombre = nombre
        self.perros = []


    def añadir_perro(self, perro):
        
        self.perros.append(perro)
        print(perro.nombre,"añadido a la lista de perros de", self.nombre )


    def listar_perros(self):

        for perro in self.perros:

            print(perro.nombre)


    def pasear_perros(self):

        print(self.nombre, "está paseando a sus perros")

        for perro in self.perros:

            perro.ladrar()




#Objetos

perro1 = Perro("Firulais","Golden",15)
perro2 = Perro("Solovino","Husky",10)

dueño = Dueño("Ana")
dueño.añadir_perro(perro1)
dueño.añadir_perro(perro2)

dueño.listar_perros()
dueño.pasear_perros()

#Usaros

#print(perro1.nombre)
#print(perro2.nombre, perro2.raza)

#perro1.ladrar()
#perro2.comer()