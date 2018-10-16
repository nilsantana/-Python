'''
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Note que

fizzbuzz(3) deve devolver Fizz

fizzbuzz(5) deve devolver Buzz

fizzbuzz(15) deve devolver FizzBuzz

fizzbuzz(4) deve devolver 4

As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas
'''

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
