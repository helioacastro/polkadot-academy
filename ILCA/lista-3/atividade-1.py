# encoding: iso-8859-1
# Calculando o Fatorial

numero = int(input("D� um n�mero para calcular o fatorial"))
fatorial = 1

for valor in range(1,numero + 1):
    fatorial = fatorial * valor
    print(valor)

print("Fatorial de ", numero, "! = ", fatorial)