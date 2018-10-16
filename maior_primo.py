'''Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
como parâmetro e devolve o maior número primo menor ou igual ao número passado
à função'''
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

def maior_primo(inteiro):
    MP = 1
    for i in range (1,inteiro+1):
        primo = eprimo(i)
        if primo >= MP:
            MP = primo
            
   
    return MP 

    '''if x > y :
        return x
    else:
        return y'''
