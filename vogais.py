'''
Escreva a função vogal que recebe um único caractere como parâmetro
e devolve True se ele for uma vogal e False se for uma consoante.
'''
def vogal (vogal):
    
    if (vogal) in ("a,A,e,E,i,I,o,O,u,U"):
        vogal = True
    else:
        vogal = False
    
    return vogal
 
