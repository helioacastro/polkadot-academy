# encoding: iso-8859-1

def ParImpar(num):
    if num % 2 == 0:
        # Numero par
        print("O n�mero ", num ," � Par")
    else:
        # Numero impar
        print("O n�mero ", num , " � �mpar")


numero = int(input("Digite o um n�mero para verificar se � par ou �mpar: "))

ParImpar(numero)
