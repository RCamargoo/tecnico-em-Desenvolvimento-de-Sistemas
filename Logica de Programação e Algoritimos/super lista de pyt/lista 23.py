linhas = int (input("digite : "))
colunas  = int (input("digite : "))
matriz = []
soma = 0 

for i in range (linhas):
    linha = []
    for j in range (colunas):
        linha .append(int(input("digite um numero : ")))
        matriz. append(linhas)

for i in range (linhas):
    for j in range (colunas ):
        soma = soma + matriz [i][j]
        print("A soma é ", soma )