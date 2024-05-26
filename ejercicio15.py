def edades():

    edad=[24, 56, 18, 25, 15, 13, 12 ,10, 19, 21, 23, 13]
    mayor =[]
    menor=[]

    for i in edad:

        if i >= 18:
            mayor.insert(i,i)

        else:
            menor.insert(i,i)

    print(f"Lista de menores {menor} /n lista de mayores {mayor}")

edades()
        