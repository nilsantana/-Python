'''
Verificar se um número inteiro é primo usando indicadores de passagem booleanos
'''
import math

total = int(input("Digite um número inteiro: "))
primo = True
n = 2
while (n <=(math.sqrt(total))and primo):
    resto = total% n
     
    if resto == 0:
        primo = False
    n = n+1
    
if primo:
    print("%d é primo"%total, primo)
else:   
    print("%d não é primo"%total, primo) 
