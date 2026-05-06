#solicita um texto para o usuario
texto = input("digite um texto qualquer: ")

#traduzir letra por letra
 
for letra in texto:   
    print(letra)

#contar quantidde  de caracteres != ''
qtd_caraquiteres = 0 

for letra in texto :
    if (letra != " "):
        qtd_caraquiteres+=1
print("A quantidade de caracters é : ", qtd_caraquiteres)

#contar a quantidade de vogais

vogais = "aeiouAEIOUáàãâÁÀÂÃéèêÉÈÊíìîÍÌÎóòôõÓÒÕÔúùûÚÙû"

qtd_vogais = 0 
for vogal in vogais :
    for letra in texto:
        if (letra == vogal):
        
            qtd_vogais+=1
print("A quantidade de vogais é :", qtd_vogais)

#palindromo 

texto_invertido = ""

for i in range(len(texto)-1,-1,-1):
    texto_invertido = texto_invertido + texto [i]

if(texto == texto_invertido):
    print("É palindromo ! ")
else:
    print("não é palíndromo")

                                