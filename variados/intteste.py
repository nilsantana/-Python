def remove_repetidos(lista):
    '''
    Função que ordena e em seguida copia para uma nova
    lista os valores não repetidos
    '''    
    ordena = sorted(lista) #ordena a lista recebida substituido pelo lista.sort()
    #lista.sort() ## uso do lista.sort() evitando gerar um novo vetor / economia consuumo memória
    ordenado=[] #vetor que receberá os valores ordenados e não repetidos
    for x in range(len(ordena)): #laço para percorrer o vetor do índice 0 até o final
        if not ordena[x] in ordenado: # verifica se não há o valor  no vetor ordenado
            ordenado.append(ordena[x]) #se não houver o valor é incluido
            
    return ordenado

relacao = [22, 4, 6, 8, 10, 12, 4, 16, 18, 20, 22, 4, 26, 8, 3]
print("Lista de %d elementos antes de ordenar e remover os duplicados"%(len(relacao)),relacao)

restantes = remove_repetidos(relacao)

print("\nApós ordenada e removido os duplicados ficou com %d elementos"%(len(restantes)),restantes)
print("\nLista de %d elementos após ordenar e remover os duplicados"%(len(relacao)),relacao)
#print("Total de elementos restantes",(len(restantes)))
