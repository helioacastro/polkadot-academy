# encoding: iso-8859-1

soma = 0
numero = 0

while numero == 0:
    numero = int(input("Digite um número, ou zero para terminar"))
    soma = soma + numero

print("A soma dos números é: ", soma)