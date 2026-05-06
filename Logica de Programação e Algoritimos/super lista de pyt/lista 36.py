numeros = []

while True:
    entrada = input("Digite um número: ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

unicos = set(numeros)

print(list(unicos))

#pesquisei essa estrutura 