#Actualizar valores de un diccionario

dic = {
    "Iphone 15 pro max": 25000,
    "Samsung Galaxy Fold 5": 42000,
    'Sony Bravia 98" ' : 127000,
    "Sonos ARC" : 19999,
    "Sonos Sub 3" : 18000,
    "Sonos Five" : 12000

}


for precio in dic.values():

    print(f"precio con el 20% de descuento: {precio* 0.8} ")

