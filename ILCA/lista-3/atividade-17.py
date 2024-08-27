# encoding: iso-8859-1

# Lista com os 50 primeiros numeros primos
# Desta forma o m�ximo n�mero perfeito � o oitavo n�mero: 2305843008139952128
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
resultado = []
soma = 0

def gera_divisores(num):
    # Faz a chamada da fun�?o recursiva divisores()
    # Ap�s o processamento da vari�vel resultado,
    # � realizado o p�s-processamento dos divisores repetidos, multiplicando-os
    # al�m de adicionar o divisor 1 comum a todos os n�meros
    
    divisores(num)
    resultado.append(1)

    anterior = resultado[0]
    for i in range(1,len(resultado)):
        if anterior == resultado[i]:
            resultado[i] = resultado[i-1] * resultado[i]
        else:
            anterior = resultado[i]

def divisores(num):
    if (num > 1):

        for primo in primos:
            if (num % primo == 0):  #�� divis�vel pelo fator primo
                fator_primo = primo

                if (num != fator_primo): #Noo busca novos divisores quanto o numero eh um numero primo
                    # Divide o numero para encontrar o divisor
                    divisor = int(num/primo)
                    
                    # Adiciona o valor encontrado na lista
                    resultado.append(divisor)

                    # Chamada recursiva para identificar outros divisores a partir do divisor encontrado
                    divisores(divisor)

                    # Adiciona o divisor primo se nao estiver na lista
                    resultado.append(fator_primo)

                break  # Interrompe o loop quando localizar o menor divisor


numero = int(input("Informe um numero para verificar se e perfeito "))

gera_divisores(numero)
resultado.sort(reverse=True)

for n in resultado:
    soma = soma + n

print("Divisores = " , resultado)
print("Soma dos divisores = ", soma)
if (numero == soma):
    print("E um numero perfeito")
else:
    print("Nao e um numero perfeito")