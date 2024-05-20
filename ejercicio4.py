import math

b = float(input("b = "))
a = float(input("a = "))
c = float(input("c = "))


root = b**2 - 4*a*c

if root < 0:
    print("La ecuación no tiene soluciones reales.")
else:

    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    print("solución 1 =", x1, "solución 2= ", x2)
