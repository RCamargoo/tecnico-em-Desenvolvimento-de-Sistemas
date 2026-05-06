pos = 0
neg = 0

for i in range(10):
    num = int(input("Digite o número: "))

    if num > 0:
        pos += 1

    elif num < 0:
        neg -= 1

print("Quantidade de positivos:", pos)
print("Quantidade de negativos:", neg)
