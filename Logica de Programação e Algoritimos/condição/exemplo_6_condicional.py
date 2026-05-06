valorCompra = float(input("Digite o valor da compra? "))
cupomDesconto = input("Possui cupom de desconto? ")

if(valorCompra >= 200 or cupomDesconto == "sim"):
    print("você ganhou um desconto de 15% !")
else:
    print("Você não tem um desconto no moento!")