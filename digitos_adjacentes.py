total = int(input("Digite um número inteiro: "))
comp = 0
ant = 0
adjacente = False
while total > 0 and not adjacente:
    ant = total % 10 
    total = total//10
    comp = total % 10
    if comp == ant:
        adjacente = True
        print("sim")
if not adjacente:
    print("não")
 
