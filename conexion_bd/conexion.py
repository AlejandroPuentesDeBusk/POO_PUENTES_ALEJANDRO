import os

os.system('cls')

import mysql.connector

#Datos, root es para cceder a todo y ahun no tenemos contraseña
connection = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = 'Agencia'
)

if connection.is_connected():

    print("The Connection was Succesfull")

#Manejar consultas

#Crear objeto
cursor = connection.cursor()
#CONSULTA QUE HACEMOS
#cursor.execute("SELECT * FROM vehiculo")
#QUE LO REGRESE
#result = cursor.fetchall()

#for fila in result:

    #print(fila)


cursor.execute("INSERT INTO `vehiculo`(`nombre`, `id_vendedor`) VALUES ('PORSHE TYCAN','1')")

connection.commit()

cursor.close()
connection.close()