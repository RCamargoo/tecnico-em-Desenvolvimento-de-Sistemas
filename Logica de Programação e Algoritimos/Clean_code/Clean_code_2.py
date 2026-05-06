notas = []

for i in range (4):
    # tenta solicitar as notas

    try:
        nota  = float(input(f"Digite a {i+1}ª nota : "))

        if(nota < 0 or  nota > 10):
            print ("Nota invalida. Insira um valor entre 0 e 10")
            exit()
        else:
            notas.append(nota)

# se tivr algum erro de valor (exesão), retomar uma mensagem 
    except ValueError :
        print("ERRO: insita um número valido!!! ")

if not notas :
    print ("ERRO: nenhuma nota foi inserida !")
else :
    media = sum (notas )/ len (notas )

    if(media >= 7):
        print(f"média = {media} - Aprovado")
    elif(media >= 5 ):
        print(f"média = {media} - recuperação")
    else:
        print(f"média = {media} - Reprovado ")