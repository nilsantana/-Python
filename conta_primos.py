
##Escreva a função n_primos que recebe um número inteiro maior ou igual a 2
##como parâmetro e devolve a quantidade de números primos que existem
##entre 2 e n (incluindo 2 e, se for o caso, n)'''
import math
def eprimo(total):
    primor = 1
    resto = 1
    n = 2
    while (n <=(math.sqrt(total)) and resto!=0):
        resto = total% n
         
        if resto == 0:
           total=total+0 
         
        n = n+1
       
    if resto!=0:
       primor = total
     
    return primor

def n_primos (inteiro):
    quantprimo=0
    MP=0
    for i in range (2,inteiro+1):
        primo = eprimo(i)
        if primo >= MP:
            MP = primo
            quantprimo= quantprimo+1
    return quantprimo
n_primos(6)
n_primos(15)
n_primos(20)
n_primos(24)
