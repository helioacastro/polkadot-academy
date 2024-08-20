# encoding: iso-8859-1

def celsiusToF(grau):
    return (grau * 9 /5) + 32

def celsiusToK(grau):
    return grau + 273.15

temperatura = int(input("Informe a temperatura em celsius: "))

print("É equivalente em Fahrenheit a ", celsiusToF(temperatura))
print("E em Kelvin é igual a ", celsiusToK(temperatura))