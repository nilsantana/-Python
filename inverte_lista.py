sequencia = []
entrada = int(input("Digite os valores desejados para inverte e 0 para sair: "))

while entrada != 0:
    sequencia.append(entrada)
    entrada = int(input("Digite um número: "))

for x in range(len(sequencia)-1,-1,-1):
    print(sequencia[x], end=", ") 
        
##Programa que recebe uma sequência de números inteiros terminados por 0
##e imprima todos os valores em ordem inversa.
##Note que 0 (ZERO) não deve fazer parte da sequência.

