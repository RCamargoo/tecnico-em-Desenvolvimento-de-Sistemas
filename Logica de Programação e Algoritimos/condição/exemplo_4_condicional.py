num1 = int(input("Digite o número 1: "))
num2 = int(input("digite o número 2: "))

operacao = input("Digite a operação (+,-,*,?/): ")


if(operacao == "+"):
    resultado = num1+num2

elif(operacao == "-"):
    resultado = num1-num2

elif(operacao == "*"):
    resultado = num1*num2

elif(operacao == "/" and num2 != 0):
    resultado = num1/num2

else:
    resultado = "❌ERRO❌"

print("O resultado é :", resultado)