numeros = []
for i in range(8):
    num = float(input("Digite o número: "))
    numeros.append(num)

# a partir daqui foi tudo pesquisado!!!

n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):

        if numeros[j] < numeros[j+1]:
            temp = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = temp

print(numeros)
