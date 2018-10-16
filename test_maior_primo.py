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
          #print("não primo",total)
        n = n+1
       
    if resto!=0:
       primor = total
       #print("primo", total)
    return primor

def maior_primo(inteiro):
    MP = 1
    for i in range (1,inteiro+1):
        primo = eprimo(i)
        if primo >= MP:
            MP = primo
            
    print("maior_primo, i",primo)
    print("maior_primo, eprimo(MP)", MP )
    return MP 
        
    '''if x > y :
        return x
    else:
        return y'''
def test_maior_primo():
    assert eprimo(997) == 997
    assert eprimo(991) == 991
    assert eprimo(983) == 983
    assert eprimo(443) == 443
    assert eprimo(349) == 349
    assert eprimo(577) == 577
    assert eprimo(401) == 401
    assert eprimo(307) == 307
    assert eprimo(211) == 211
    assert eprimo(101) == 101
    assert maior_primo(103) == 103
    assert maior_primo(408) == 401
    assert maior_primo(1000) == 997
    assert maior_primo(910) == 907
    assert maior_primo(725) == 719
    assert maior_primo(430) == 421
    assert maior_primo(918) == 911
    assert maior_primo(97) == 97
    assert maior_primo(71) == 71
    assert maior_primo(211)== 211
