# encoding: iso-8859-1

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
print("Qual o intervalo de números para checar os números primos?")
inicio = int(input("A partir do número: "))
fim = int(input("Até o número: "))

for numero in range(inicio, fim):
    if eh_primo(numero):
        print(numero)


