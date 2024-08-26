# Lista com os 50 primeiros números primos
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
resultado = []
soma = 0

def divisores(num):
    if (num > 1):

        for primo in primos:
            if (num % primo == 0):  #É divisível pelo fator primo
                fator_primo = primo

                if (num != fator_primo): #Não busca novos divisores quanto o número é um número primo
                    # Divide o número para encontrar o divisor
                    divisor = int(num/primo)
                    
                    # Adiciona o valor encontrado na lista
                    resultado.append(divisor)

                    # Chamada recursiva para identificar outros divisores a partir do divisor encontrado
                    divisores(divisor)

                # Adiciona o divisor primo se não estiver na lista
                if (fator_primo < resultado[-1]):
                    resultado.append(fator_primo)

                break  # Interrompe o loop quando localizar o menor divisor
            
    else:
        resultado.append(1)

numero = int(input("Informe um número para verificar se é perfeito "))

divisores(numero)
for n in resultado:
    soma = soma + n

print("Divisores = " , resultado)
print("Soma dos divisores = ", soma)
if (numero == soma):
    print("É um número perfeito")
else:
    print("Não é um número perfeito")