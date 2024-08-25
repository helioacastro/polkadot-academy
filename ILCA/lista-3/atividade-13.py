
soma_pares = 0

for i in range(100):
    numero= i + 1
    
    if numero % 2 == 0:
        soma_pares = soma_pares + numero

print("A soma dos numeros pares entre 1 e 100 é ", soma_pares)
