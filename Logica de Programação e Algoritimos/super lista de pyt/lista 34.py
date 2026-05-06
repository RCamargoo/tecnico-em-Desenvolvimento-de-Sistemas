matriz = []

for i in range (2):
    linha = []
    for j in range (3):
        linha.append(int(input("digite um número : ")))
    matriz.append(linha)

for i in range (2):
    for j in range (3):
        matriz [i][j] = matriz [i][j]*2

print(matriz)
