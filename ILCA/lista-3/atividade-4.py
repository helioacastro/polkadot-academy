# encoding: iso-8859-1

def palindromo_teste(palavra):
    palavra = palavra.upper()
    palavra_invertida = ""

    for letra in palavra:
        palavra_invertida = letra + palavra_invertida

    if(palavra == palavra_invertida):
        print("Palíndromo")
    else:
        print("N?o é um palíndromo")


teste_palavra = input("Digite uma palavra para checar se é um palíndromo: ")
palindromo_teste(teste_palavra)
