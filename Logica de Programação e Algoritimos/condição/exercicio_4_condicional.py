lado1 = int(input("digite lado 1: "))
lado2 = int(input("digite lado 2: "))
lado3 = int(input("digite lado 3: "))

if ((lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3 ) > lado2):
    if(lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
        print("equilatero")
    elif(lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
        print("escaleno")

    else:
        print("isóceles")
else:
    print("O triangulo não existe! 1")
