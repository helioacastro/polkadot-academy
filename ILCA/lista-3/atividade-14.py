numero1 = int(input("Informe um número "))
numero2 = int(input("Informe outro número "))

operador = input("Qual operação vai ser realizada? (* / + -)")

match operador:
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 / numero2
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case _ :
        resultado = None

if resultado != None:
    print("O resultado é ", resultado)
else:
    print("Operador inválido")

