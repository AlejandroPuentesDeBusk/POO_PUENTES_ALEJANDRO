dic= { 
    "hola" : "saludar",
    "carro" : "cosa con ruedas",
    "playera" : "cosa que te pones",
    "telefono" : "cosa para hablar",

     }

buscar = str(input("Ingrese palabra "))

if buscar in dic:

    print(dic[buscar])