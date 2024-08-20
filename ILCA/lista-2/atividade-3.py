# encoding: iso-8859-1

# Calculo de IMC

peso = float(input("Favor informar o seu peso: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso / (altura * altura)

print("O seu IMC é ", imc)