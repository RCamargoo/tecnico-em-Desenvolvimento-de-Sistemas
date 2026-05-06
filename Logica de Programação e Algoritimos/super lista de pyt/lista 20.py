maiores = 0

for i in range(1, 7):
    idade = int(input("Digite a  idade: "))
    
    if idade >= 18:
        maiores += 1

print("Total de pessoas maiores de idade:", maiores)
