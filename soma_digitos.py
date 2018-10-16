'''
programa para somar os digitos de um dado algarismo
exemplo: 123 retorna 6
         45 retorna 9

'''

total = int(input("Digite um número inteiro: "))
soma = 0
fim = False
while (not fim):
    soma = total % 10 + soma 
    total = total // 10
    if total == 0:
        fim = True
print(soma)
