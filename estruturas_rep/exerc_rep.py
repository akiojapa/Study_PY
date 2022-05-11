#Exercicio 1: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

"""
conf = False
while conf == False:

    sal = float(input("Digite quantos reais você ganha por hora: "))
    hora = int(input("Digite a quantidade de horas que você trabalha por mês: "))
    if sal < 0:
        print("Digite um número acima de 0\n\n")
    elif 0 < hora > 744:
        print("Digite um número que bata com as horas do mês(0 - 744)\n\n")
    else:
        conf = True
        tot = sal
        for h in range(1, hora):
            tot = tot + sal
print(f"O salário total por mês é: {tot}")
"""

"""
#Exercicio 2: Faça um Programa que peça dois números e imprima a soma

x, y = input("Digite dois números inteiros para descobrir sua soma(x,y): \n").split(",")

x = int(x)
y = int(y)
tot = 0
for n in range(0, y + x):
    tot = tot + 1

print(f"A soma dos números é {tot}")
"""

"""
#Exercicio 3: Faça um Programa que peça as 4 notas bimestrais e mostre a média.

media = 0
for n in range(0,4):
    x = float(input(f"Digite sua nota do {n + 1}º bimestre: "))
    media = media + x;

print(f"A média das notas bimestrais é: {media / 4}")
"""
"""
#Exercicio 4: Faça um Programa que peça 2 números,um inteiro e um número real. Calcule e mostre o produto do dobro do
# primeiro com metade do segundo
conf = False

while conf == False :
    for n in range(0,2):

        if(n < 1):
            x = int(input(f"Digite o {n + 1}º número(inteiro): \n"))
            tot = x * 2
        else:
            x = float(input(f"Digite o {n + 1}º número(real):\n "))
            tot = tot * (x / 2)
            conf = True
            print(f"O produto do dobro do primeiro com a metade do segundo é: {tot}")
"""


#A partir daqui achei melhor utilizar listas(vetores) para trabalhar com os métodos de repetição.
"""
#Exercicio 5: Faça um Programa que peça dois números e imprima o maior deles


num = []
for n in range(0,2):
    x = int(input(f"Digite o número {n + 1}º : "))
    num.append(x)




for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

print(f"O maior número é: {num[0]}")
"""

"""
#Exercicio 6: Faça um Programa que leia três números e mostre o maior deles.
num = []
for n in range(0,3):
    x = int(input(f"Digite o número {n + 1}º : "))
    num.append(x)




for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

print(f"O maior número é: {num[0]}")
"""

"""
# Exercicio 7: Faça um Programa que leia três números e mostre o maior e o menor deles.
num = []
for n in range(0,3):
    x = int(input(f"Digite o número {n + 1}º : "))
    num.append(x)




for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

print(f"O maior número é: {num[0]}\n")
print(f"O menor número é: {num[2]}\n")
"""

"""
#Exercicio 8: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

num = []
for n in range(0,3):
    x = float(input(f"Digite o preço do {n + 1}º produto: "))
    num.append(x)




for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

print(f"O produto mais barato para se comprar é: {num[2]}\n")
"""

"""
#Exercicio 9: Faça um Programa que leia três números e mostre-os em ordem decrescente.

num = []
for n in range(0,3):
    x = int(input(f"Digite o {n + 1}º número: \n"))
    num.append(x)


print("Ordem decrescente:")


for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp


for m in range(0, len(num)):
    print(f"{num[m]}")
"""

#Exercicio 10: Faça um Programa que peça os 3 lados de um triângulo e verifique se é verdadeiro

#Tive uma pequena dificuldade neste ponto para utilizar somente a repetição na hora da validação do triângulo, portanto
#só ordenei em uma lista mesmo


num = []
for n in range(0,3):
    x = int(input(f"Digite a medida do {n + 1}º lado do triângulo: \n"))
    num.append(x)




for i in range(0, len(num)):
    for j in range(i, len(num)):
        if num[j] > num[i]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

aux = 0
for n in range(0, len(num)):

    if num[n] < (sum(num) - num[n]):
        for m in range(0, len(num)):
            if num[m] == num[n]:
                aux = aux + 1
            elif num[m] != num[n]:
                aux = aux + 2
    else:
        aux = 0
        print("Não é possível existir um triângulo a partir destes lados")

print(aux)
if aux == 9:
    print("Os lados formam um triângulo equilátero.")
elif aux == 13:
    print("Os lados formam um triângulo isósceles.")
elif aux == 15:
    print("Os lados formam um triângulo escaleno.")






