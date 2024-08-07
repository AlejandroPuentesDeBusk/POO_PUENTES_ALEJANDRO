graficas = {
    "Titan RTX": 2500,
    "4090 TI": 4000,
    "3080 TI" : 3200,
    "2080 SUPER": 2500
    }

#Agregar clave y valor
graficas["AMD 6900 XT"] = 3000

#borrar una clave

del graficas["2080 SUPER"]

print(graficas)