# encoding: iso-8859-1

def ParImpar(num):
    if num % 2 == 0:
        # Numero par
        print("O número ", num ," é Par")
    else:
        # Numero impar
        print("O número ", num , " é Ímpar")


numero = int(input("Digite o um número para verificar se é par ou ímpar: "))

ParImpar(numero)
