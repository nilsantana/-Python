n = int(input("Digite um número inteiro maior que 1: "))
fator = 2
multiplicidade = 0

while n > 1:    
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:    
        print("Fator é %d e a multiplicidade é %d" %(fator, multiplicidade))
    fator = fator + 1
    multiplicidade = 0          
