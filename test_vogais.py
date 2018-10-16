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
 
def test_vogal():
    assert vogal("a") == True
    assert vogal("A") == True
    assert vogal("e") == True
    assert vogal("E") == True
    assert vogal("i") == True
    assert vogal("I") == True
    assert vogal("o") == True
    assert vogal("O") == True
    assert vogal("u") == True
    assert vogal("U") == True
    assert vogal("b") == False
    assert vogal("c") == False
    assert vogal("B") == False
    assert vogal("V") == False
    assert vogal("1") == False
