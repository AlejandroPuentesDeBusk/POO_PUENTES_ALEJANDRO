#CLASE
class Perro:
    def _init_(self, nombre, raza, edad): 
        self.nombre = nombre 
        self.raza = raza 
        self.edad = edad 
        self.collar = None
    
    def ladrar(self):
        print("GUAF")
        
    def comer(self):
        print("Comiendo...")
    
    def poner_collar(self, collar):
        self.collar = collar
    
    def describir(self):
        print("Soy un perro llamado", self.nombre,
              "soy de raza", self.raza, "y tengo",
              self.edad, "años.")
        if self.collar:
            print("Llevo puesto un collar de color",
                self.collar.color, "y material", self.collar.material)
    
    def jugar(self, juguete):
        print(self.nombre, "esta jugando con el juguete", 
              juguete.nombre)           



#DEPENDENCIA
class Juguete:
    def _init_(self, nombre,material):
        self.nombre= nombre
        self.material=material
        
    def describir(self):
        print(self.nombre,"Esta hecho de", 
              self.material)