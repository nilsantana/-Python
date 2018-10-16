def fizzbuzz (num):
    tri = num % 3
    qui = num % 5

    if tri == 0 and not qui == 0:
         return ("Fizz")
    elif not tri == 0 and qui == 0:
         return ("Buzz")
    elif tri == 0 and qui == 0:
         return ("FizzBuzz")
    else:
        return(num)
        
def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(4) == 4
