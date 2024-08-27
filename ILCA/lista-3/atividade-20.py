# encoding: iso-8859-1
numeros = []

while True:
    numero = int(input("Informe um numero para a lista (digite 0 para terminar): "))

    if (numero == 0):
        break
    else:
        numeros.append(numero)
print(numeros)

maior = numeros[0]
menor = numeros[0]
soma = 0
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    soma = soma + numeros[i] 

print("O maior numero eh: ", maior)
print("O menor numero eh: ", menor)
print("A media eh: ", soma / len(numeros))



