# encoding: iso-8859-1

n = int(input("Informe o valor n da sequencia de Fibonacci "))

# Insere o primeiro item da sequencia fibonacci
fibonacci = [1]
i=0

while n>i+1:
    # Inserir o segundo item com valor igual a 1
    if i == 0:
        fibonacci.append(1)
    # A partir do terceiro item, insere-se a soma dos dois itens anteriores
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i])
    
    i = i + 1

print(fibonacci)