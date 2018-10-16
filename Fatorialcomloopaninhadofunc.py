def fatorial(n):
    
        fatorial = 1
        while n > 1:
            fatorial = fatorial *n
            n = n -1
        print("Fatorial é %d" %fatorial)
        #n = int(input("Digite um número inteiro: "))

def main():
    x = 1
    while x > 0:
        x = int(input("Digite um número inteiro maior que zero ou zero para sair: "))
        fatorial(x)
