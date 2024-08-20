# encoding: iso-8859-1
# Calculando o Fatorial

numero = int(input("Dê um número para calcular o fatorial"))
fatorial = 1

for valor in range(1,numero + 1):
    fatorial = fatorial * valor
    print(valor)

print("Fatorial de ", numero, "! = ", fatorial)