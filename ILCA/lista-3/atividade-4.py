# encoding: iso-8859-1

def palindromo_teste(palavra):
    palavra = palavra.upper()
    palavra_invertida = ""

    for letra in palavra:
        palavra_invertida = letra + palavra_invertida

    if(palavra == palavra_invertida):
        print("Pal�ndromo")
    else:
        print("N?o � um pal�ndromo")


teste_palavra = input("Digite uma palavra para checar se � um pal�ndromo: ")
palindromo_teste(teste_palavra)
