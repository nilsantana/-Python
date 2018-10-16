'''
v1 - Verificar se um número inteiro é primo sem usar indicadores de passagem booleanos
v2 -ajustado para usar função
'''
import math
total = 1
#total = int(input("Digite um número inteiro: "))
def primalidade(total):
    resto = 1
    n = 2
    while (n <=(math.sqrt(total)) and resto!=0):
        resto = total% n
         
        if resto == 0:
            print("não primo")
        n = n+1
        
    if resto!=0:
        print("primo")
  #trecho testando loop
while total!= 0:
    total = int(input("Digite um número inteiro ou 0  para sair: "))
    primalidade(total)
