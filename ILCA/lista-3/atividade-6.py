# encoding: iso-8859-1

frase = input("Digite uma frase: ")
vogais = ["a","e","i","o","u"]
num_vogais = 0

for letra in frase:
    if letra.lower() in vogais:
        num_vogais = num_vogais + 1

print("Total de vogais encontras é ", num_vogais)