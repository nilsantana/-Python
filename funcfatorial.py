def fatorial(n):
    fatorial = 1
    while (n>1):
        fatorial = fatorial*n
        n = n-1
    return fatorial

v = int(input("Digite o valor para calcular o fatorial "))
fatorado = fatorial(v)
print("Fatorial de %d é: %d "%(v,fatorado))
