import math

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
x1 = int(input("Digite o valor de x1: "))
y1= int(input("Digite o valor de y1: "))

dist = math.sqrt((x1-x)**2+(y1-y)**2)

if dist >= 10:
     print("longe")

else:
    print("perto")
