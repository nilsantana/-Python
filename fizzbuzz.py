num = int(input("Digite um número inteiro: "))

qui = num % 5
tri = num % 3
if qui == 0 and tri == 0:
     print("FizzBuzz")

else:
    print(num)
