# encoding: iso-8859-1

def gerar_tabuada(numero):
    for item in range(10):
        print(numero, "x", item+1, "=", numero * (item + 1))
        
tabuada = int(input("Informe de qual número deseja a taboada: "))
gerar_tabuada(tabuada)
