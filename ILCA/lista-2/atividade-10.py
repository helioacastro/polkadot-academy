# encoding: iso-8859-1

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
print("Qual o intervalo de n�meros para checar os n�meros primos?")
inicio = int(input("A partir do n�mero: "))
fim = int(input("At� o n�mero: "))

for numero in range(inicio, fim):
    if eh_primo(numero):
        print(numero)


