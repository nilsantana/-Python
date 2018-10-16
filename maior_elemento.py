def maior_elemento(lista):
    '''
    Função maior_elemento que recebe como parâmetro uma lista com números inteiros
    e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
    '''
    lista.sort()
    maior = lista[len(lista)-1]


    return maior

relacao = [22, 4, 6, 8, 10, 12, 4, 16, 18, 20, 22, 4, 26, 8, 3]
print("Lista de %d elementos antes de verificar maior elemento"%(len(relacao)),relacao)

verificado = maior_elemento(relacao)

print("\nMaior elemento da lista é %d. "%verificado)
