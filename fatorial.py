n = int(input("Digite o valor de n: "))
fatorial = n
valor = n
while (n>1):
    fatorial = fatorial*(n-1)
    n = n-1
if fatorial == 0:
    print("O fatorial de %d é 1" %n)
else:   
    print("O fatorial de %d é %d" %(valor,fatorial))    
