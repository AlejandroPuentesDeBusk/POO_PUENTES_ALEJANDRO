
#Creamos lista
list = ["alejandro","franc","edson","harry","blanca","caro"]

#Modificar posición en al lista
list[2] = "sexon"

#agrega elemento al final
list.append("enano")

#agrega elemento donde le digas
list.insert(6, "Valeria")

#fusiona dos listas
list.extend(["ana", "ricardo", "jose"])

#para remover elemento de lista, pero indicas que dise
list.remove("franc")

#elimina el elemento pero muestra cual borraste
element = list.pop(5)
print(element)

#Imprimir un elemento de la lista
print(list[2])

print(list)