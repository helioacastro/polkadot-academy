import random

alvo = random.randint(1,100)
#print(alvo)
while True:
    palpite = int(input("Digite seu palpite "))

    if palpite > alvo:
        print("Errado, o valor é menor")
    elif palpite < alvo:
        print("Errado, o valor é maior")
    else:
        print("Você acertou!! O número é ", alvo)
        break




print(alvo)