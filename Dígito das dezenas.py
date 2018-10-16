numero = input("Digite um número inteiro: ")
dezena = len(numero)
dezena = dezena - 2
if (dezena < 0):
    print("O dígito das dezenas é 0")
else:    
    print("O dígito das dezenas é",numero[dezena ])
