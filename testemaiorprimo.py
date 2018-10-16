import math
def eprimo(total):
    primor = int
    resto = 1
    n = 2
    while (n <=(math.sqrt(total)) and resto!=0):
        resto = total% n
         
        if resto == 0:
          print("não primo",total)
        n = n+1
       
    if resto!=0:
        
       # print("primo", total)
        primor = total*1
        return primor

def maior_primo(inteiro):
    for i in range (1,inteiro):
        eprimo(i)
        #print("maior_primo, i",primor)
        #print("maior_primo, eprimo(i)",eprimo(i) )
    return 
