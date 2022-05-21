import math

a = float(input("Digite o valor de 'A': "))
b = float(input("Digite o valor de 'B': "))
c = float(input("Digite o valor de 'C': "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    Raiz1 = (-b + math.sqrt(delta)) / (a * 2)
    print("A única raiz é", Raiz1)
else: 
    if delta < 0:
        print("Essa equação não possui números reais")
    Raiz1 = (-b + math.sqrt(delta)) / (a * 2)
    Raiz2 = (-b - math.sqrt(delta)) / (a * 2)
    print("A primeira raiz é: ", Raiz1)
    print("A segunda raiz é: ", Raiz2)
    
