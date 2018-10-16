def soma_elementos(lista):
 

    somadalista = 0
    for x in range(len(lista)):
        item = lista[x]
        somadalista = somadalista + item
    return somadalista

relacao = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 3]
somadalista = soma_elementos(relacao)
print("soma da lista é",somadalista)
