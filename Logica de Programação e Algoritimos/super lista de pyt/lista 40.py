texto = input("digite um texto qualquer: ")

texto_invertido = ""

for i in range(len(texto)-1,-1,-1):
    texto_invertido = texto_invertido + texto [i]

if(texto == texto_invertido):
    print("É palindromo ! ")
else:
    print("não é palíndromo")

                                