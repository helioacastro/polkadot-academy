# encoding: iso-8859-1

compras = []
flag = True

while flag:
    item = input("Digite o item de compra (zero para sair) ")

    if item != "0":
        compras.append(item)
    else:
        flag = False

# Imprimir lista
for compra in compras:
    print(compra)