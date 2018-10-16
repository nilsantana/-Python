'''
Calculo fibonacci usando recursividade 
'''

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

v = int(input("Digite o valor para calcular o fibonacci "))
fibonado = fibonacci(v-1)
print("O número de fibonacci de %d é: %d "%(v,fibonado))
