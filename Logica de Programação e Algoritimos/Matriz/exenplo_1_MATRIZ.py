matriz = [
    ["laranja","romã"," maça-verde ","limão","caqui" ],
    ["beringela","batata","pimentão","pimenta","pepino"],
]
print(matriz[0])#imprime a primera linha (fruta)
print(matriz[1])#imprime a primera linha (legume)

print(matriz[0][2])#imprime maça-verde 
print(matriz[1][3])#imprime pimenta
#forma dificil
print("frutas:  ")
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[0][3])
print(matriz[0][4])

print("legumes:  ")
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[1][3])
print(matriz[1][4])

print("matriz completa: ")
for i in range(2): #linha
    for j in range(4): #coluna
        print(matriz[i][j])
