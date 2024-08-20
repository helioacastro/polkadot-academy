# encoding: iso-8859-1

frase = input("Escreva uma frase: ")
ocorrencias = {}

for letra in frase:
    letra = letra.upper()

    if letra in ocorrencias:
        ocorrencias[letra] += 1
    else:
        ocorrencias[letra] = 1

print("Letras encontradas na frase")
for letra in ocorrencias.keys():
    if letra != " ":
        print("Letra ", letra, " = ", ocorrencias[letra])
    