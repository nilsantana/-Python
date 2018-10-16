def maximo(x,y,z):
    if x > y and x > z:
        return x
    elif x<y and y>z:
        return y
    else:
        return z

    
def test_maximo():
    assert maximo(2,5,1) == 5
    assert maximo(1,2,-2) == 2
    assert maximo(3,4,-5) == 4
    assert maximo(4,3,9) == 9
    assert maximo(0,-1,4) == 4
    assert maximo(-1,0,9) == 9
    assert maximo(50,10,40) == 50
    assert maximo(200,5,100) == 200
    assert maximo(250,-100,200) == 250
    assert maximo(300,100,10) == 300





    
