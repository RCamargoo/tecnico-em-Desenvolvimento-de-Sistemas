idade = int(input("Digite sua idade: "))
carteira = input("Voê tem CNH? ")

if(idade >= 18 and carteira == "sim"):
    print("Você pode dirigir!🚗  ")

elif(idade >= 18 and carteira =="não"):
    print("você não pode dirigir🚗 ")

elif(idade < 18 ):
    print("você não pode tirar CNH❌ ")
else:
    print("ERRO❌")





