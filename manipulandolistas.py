
###incluindo valores pares em um vetor
valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)

####imprimimdo sem retirar do vetor
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(pares[x])
### inverte a lista e retira do vetor
    flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1
#imprimindo de um indice até o (segundo indice-1)
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5, 10):
    print(pares[x])

### imprimir componentes de uma lista forma 1
    animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
    for x in animais:
    print("--> ", x)

### imprimir componentes de uma lista forma 2
    animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
    for x in range(len(animais)):
    print("--> ", animais[x])
### imprimir componentes de uma lista forma 3
    animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
    for x in animais:
	print("-" + x)


####
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")

#####################3
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")
