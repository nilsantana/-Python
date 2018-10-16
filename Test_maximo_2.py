'''
Escreva a função maximo que recebe 2 números inteiros
como parâmetro e devolve o maior deles.
'''
def maximo(x,y):
    if x > y :
        return x
    else:
        return y
    
def test_maximo():
    assert maximo(2,1) == 2
    assert maximo(1,2) == 2
    assert maximo(3,4) == 4
    assert maximo(4,3) == 4
    assert maximo(0,-1) == 0
    assert maximo(-1,0) == 0
    assert maximo(5,10) == 10
    assert maximo(10,5) == 10
    assert maximo(200,-100) == 200
    assert maximo(-200,100) == 100
