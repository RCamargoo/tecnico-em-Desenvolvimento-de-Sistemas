#codigo errado 
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a + b + c +  d)/4

if x >=7:
    print("ok")

elif x >=5:
    print("REC")

else:
    print("NO")




#Clean code

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))
nota4 = float(input("Digite nota 4: "))
media = (nota1 + nota2 + nota3 + nota4)/4

if (media >= 7):
    print("Aprovado!!!")

elif(media >= 5):
    print("Recuperação!!!")

else:
    print("Dados invalidos !!!!")




#Clean code 2 

notas = []

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota :  ")))

media = sum(notas )/len (notas)

if (media >= 7):
    print("Aprovado!!!")

elif(media >= 5):
    print("Recuperação!!!")

else:
    print("Dados invalidos !!!!")

print("Sua media é ", media )



