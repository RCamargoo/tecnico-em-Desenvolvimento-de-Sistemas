saltos = []

for i in range(7):
    saltos.append(int(input("digite o valor do salto: ")))

#todos o saltos na ordem em que foram realizado!!!
print(saltos)

#Maior
maior = saltos [0]

for salto in saltos:
    if(salto > maior ):
        maior = salto

print("O maior salto é: ", maior )

#Menor
menor = saltos [0]

for salto in saltos:
    if(salto < menor ):
        menor = salto

print("O menor salto é: ", menor )

#agora devemos ver a media dos saltos desconsiderando o maior e o menor!!!
soma = 0

for salto in saltos:
    if(salto != maior and salto != menor ):
        soma = soma + salto
media = soma / 5
print("A média sem maior e menor é : ", media )


#media geral

soma = 0

for salto in saltos:
    soma = soma + salto
media_geral = soma /7
print("A média geral :", media_geral)
