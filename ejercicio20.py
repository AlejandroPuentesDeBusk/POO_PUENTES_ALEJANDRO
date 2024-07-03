conjunto1 = {1,2,3,4,5}

conjunto2 = {6,7,8,9,10}

conjunto3 = {11,12,13,14,15}

conjunto_plus = conjunto1 | conjunto2 | conjunto3

conjunto4 = set()


def par(n):

    if n%2 == 0:

        return n

for i in conjunto_plus:

    n= par(i)

    conjunto4.add(n)


print(conjunto4)