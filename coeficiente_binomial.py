n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

def fatorial(n):
    fatorial = 1
    while (n>1):
        fatorial = fatorial*n
        n = n-1
    return fatorial


def binomial(n,k):
    return fatorial(n)//(fatorial(n-k)*fatorial(k))


print("fatorial de n ", n," é :",fatorial(n), "fatorial de k ", k," é :",fatorial(k))    
print("binomial de n sobre k é ",binomial(n,k))




