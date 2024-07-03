#CLASE
class Perro:
    def _init_(self, nombre, raza, edad): 
        self.nombre = nombre 
        self.raza = raza 
        self.edad = edad 
    
    def ladrar(self):
        print("GUAF")
        
    def comer(self):
        print("Comiendo...")
    
    def describir(self):
        print("Soy un perro llamado", self.nombre,
              "soy de raza", self.raza, "y tengo",
              self.edad, "años.")

#ASOCIACIÓN
class Veterinario:
    def _init_(self, nombre):
        self.nombre = nombre
        self.perros_atendidos = []

    def atender_perro(self, perro): 
        if perro not in self.perros_atendidos:
            self.perros_atendidos.append(perro) 
            print(self.nombre, "está atendiendo a", perro.nombre)
        else:
            print(self.nombre, "ya atendió a", perro.nombre)

    def listar_perros_atendidos(self):
        print(self.nombre, "ha tratado a los siguientes perros:")
        for perro in self.perros_atendidos:
            print(perro.nombre)

#AGREGACIÓN
class Dueño:
    def _init_(self, nombre):
        self.nombre = nombre
        self.perros = []
    
    def añadir_perro(self, perro):
        self.perros.append(perro)
        print(perro.nombre, "añadido a la lista de perros de", self.nombre )

    def listar_perros(self):
        print(self.nombre, "tiene los siguientes perros: ")
        for perro in self.perros:
            print(perro.nombre)
    
    def pasear_perros(self):
        print(self.nombre, "está paseando a sus perros: ")
        for perro in self.perros:
            perro.ladrar()

#COMPOSICIÓN


#OBJETOS
perro1 = Perro("Firulais", "Chihuahua", 3)
perro2 = Perro("Max", "Pitbull", 5)
dueño = Dueño("Ana")
veterinario1 = Veterinario("Dra. Ana")

