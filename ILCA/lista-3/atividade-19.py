# encoding: iso-8859-1

peso = [2, 3, 5]
nota = [0, 0, 0]
nota_ponderada = 0.0
numerador = 0.0
denominador = 0.0

nota[0] = float(input("Informe a primeira nota: "))

nota[1] = float(input("Informe a segunda nota: "))

nota[2] = float(input("Informe a terceira nota: "))

for i in range(len(nota)):
    numerador = numerador + (nota[i] * peso[i])
    denominador = denominador + peso[i]

nota_ponderada = numerador / denominador

print("Nota ponderada eh: ", round(nota_ponderada,2))





