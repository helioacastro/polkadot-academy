texto = input("Informe um texto a ser invertido ")
texto_invertido = ""

for i in range(len(texto)):
    texto_invertido = texto[i] + texto_invertido
    
print(texto_invertido)