# encoding: iso-8859-1

contador = 0
soma = 0
media = 0

while True:
    numero = int(input("Digite a nota a ser contabilizada, digite (-1) para terminar ")) 

    if numero == -1:
        break
    
    contador = contador + 1
    soma = soma + numero

media = soma / numero

print("A média das notas é ", media)