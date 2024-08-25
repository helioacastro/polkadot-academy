# encoding: iso-8859-1

num1 = int(input("Digite um número qualquer "))

num2 = int(input("Digite outro número "))

num3 = int(input("Digite mais outro "))

if num1 <= num2:
    p1 = num1
    p3 = num2
else:
    p1 = num2
    p3 = num1

if num3 <= p1:
    p2 = p1
    p1 = num3
else:
    p2 = p3
    p3 = num3

print("Primeiro = ", p1)
print("Segundo = ", p2)
print("Terceiro = ", p3)