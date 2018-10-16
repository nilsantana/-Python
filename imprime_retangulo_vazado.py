col = int (input("Digite a largura: "))
lin = int (input("Digite a altura: "))
L = 0
C = 0
for L in range(0,lin): # criando linhas
    for C in range(0,col):  # criando colunas
        if ( L == 0 or L == lin - 1 ): #verificando a primeira e a ultima linha e preenchendo com tralhas
            print("#" ,end="")
        elif ( L > 0 or L< lin - 1 ) and (C < 1 or C==col-1): #verificando a primeira e a última coluna e preenchendo com tralhas
            print("#",end="")
        else:
            print(" ",end="") #preeenchendo o espaço restante
        C = C + 1
    print("")#final de linha/pula para próxima linha
L = L + 1     
