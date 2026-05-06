numeros = []

for i in range(10): 
    num = int(input("digite um número: "))
    numeros.append(num)

cont_pares = 0

for numero in numeros :
    if (numero % 2 == 0):
        cont_pares = cont_pares + 1
print("a quantidade de pares foi", cont_pares)