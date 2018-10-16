'''Escreva uma função soma_hipotenusas que receba como parâmetro um número
inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n
que são comprimento da hipotenusa de algum
triângulo retângulo com catetos inteiros.'''
import math

def e_hipotenusa(h):
  cat1 = 1
  cat2 = 1
  match = 0
  while cat1 < h:# and not match:
    while cat2 < h: #and not match:
      if h == math.sqrt(cat1 ** 2 + cat2 ** 2):
        match = h
      else:
        cat2 = cat2 + 1
    cat1 = cat1 + 1
    cat2 = 1
  return match #bool(match)
    

def soma_hipotenusa(n):
    soma = 0
    i = 1
    while i < n:
        sim = e_hipotenusa(i)
        soma = soma + sim
        i = i + 1
    return soma    
