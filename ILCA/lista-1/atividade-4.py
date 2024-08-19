# encoding: iso-8859-1

temperatura = int(input("Qual a temperatura neste momento, em graus celsius?"))

if temperatura > 30:
    print("Temperatura Quente")
elif temperatura >= 15:
    print("Temperatura agradável")
else:
    print("Temperatura fria")