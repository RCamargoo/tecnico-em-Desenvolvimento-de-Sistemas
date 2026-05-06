contador = 0

while True:
    nome = input("Nome: ")

    if nome== "sair":
        break
    
    contador += 1

print("-" * 30)
print("Foram digitados", contador )
print("-" * 30)

