numeros = []
invertido = [0,0,0,0,0]

for i in range(5): 
    num = int(input("digite um número: "))
    numeros.append(num)

for i in range(5):
    invertido [i] = numeros[4-i]

print(invertido)
