'''
Algoritmo de Bhaskara refatorada em formato de função
'''

import math
def delta (a,b,c):
    return b ** 2 - 4*a*c

def main():
        a_digitado = float(input("Digite o valor de a: "))
        b_digitado = float(input("Digite o valor de b: "))
        c_digitado = float(input("Digite o valor de c: "))
        imprime_raizes(a_digitado,b_digitado,c_digitado)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d ==0:
         raiz1 = (-b + math.sqrt(d)) / (2*a)
         print("a raiz desta equação é",raiz1)
    else:
        if d < 0:
                print("esta equação não possui raízes reais")
        else:    
                 raiz1 = (-b + math.sqrt(d)) / (2*a)
                 raiz2 = (-b - math.sqrt(d)) / (2*a)
                 print("A primeira raiz é: ",raiz1)
                 print("A segunda raíz é: ",raiz2)    
                    
main()
