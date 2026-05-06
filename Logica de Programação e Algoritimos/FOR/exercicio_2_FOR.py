numero1 = int(input("digite seu nùmero 1: "))
numero2 = int(input("digite seu nùmero 2: "))
soma = 0

for i in range(numero1, numero2+1):
    if (i%2==0):
        soma = soma +i

print(soma)

