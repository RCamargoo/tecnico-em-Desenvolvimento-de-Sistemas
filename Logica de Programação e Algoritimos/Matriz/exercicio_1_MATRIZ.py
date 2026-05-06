matriz_1 = []
matriz_2 = []
m_soma = []

#preencher matriz (repetir sempre que preencher matriz)
for i in range (3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"matriz_1[{i}][{j}] = ")))
    matriz_1.append(linha)

#preencher matriz (repetir sempre que preencher matriz)
for i in range (3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"matriz_2[{i}][{j}] = ")))
    matriz_2.append(linha)

#preencher matriz (repetir sempre que preencher matriz)
for i in range (3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"matriz_1[i][j]+matriz_2[i][j] ")))
    m_soma.append(linha)

#exibir matriz (repetir sempre que exibir matriz)
print("matriz soma : ")
for linha in m_soma:
        print(linha)





  


  