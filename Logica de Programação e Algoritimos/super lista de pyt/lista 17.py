palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOUáàâãÃÂÀÁÊÈÉéèêÌÍÎîíìÒÓÔôõóòÚÙÛúùû"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("A palavra ",palavra," possui ",contador," vogais.")
