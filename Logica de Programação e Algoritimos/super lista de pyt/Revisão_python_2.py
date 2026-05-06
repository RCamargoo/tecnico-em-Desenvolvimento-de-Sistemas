#Revisão matrz 1
# Solicitar a quantidade de linha 
# solicitar a quntidade de coluna 
# preencher a matriz
# calcular a soma de todos os números


linhas = int (input("Digite a quantidade de linhas: "))
colunas = int (input("Digite a quantidade de colunas : "))
matriz = []
soma = 0 

for i in range(linhas):
    linha = []
    for j in range (colunas ):
        linha. append(int(input("digite um número: ")))
        matriz.append(linha)

for i in range (linhas):
    for j in range (colunas ):
        soma = soma + matriz[i][j]
        print("A soma é :", soma )
