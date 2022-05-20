import random

#Exercício 1: Escreva um programa que some todos os itens de uma lista

"""
num = int(input("Escreva quantos números deseja somar: \n"))

nums = []

n = 1
while n <= num:
    elemento = int(input(f"Digite o {n}º número inteiro: "))
    nums.append(elemento)
    n = n + 1


print(sum(nums))
##SEM FUNÇÃO

soma = 0

for n in range(0, num):
    soma = soma + nums[n]

print(soma)
"""

#Exercicio 2: Escreva um programa que multiplique todos os itens de uma lista.


"""
num = int(input("Escreva quantos números deseja multiplicar: \n"))

nums = []

n = 1
while n <= num:
    elemento = int(input(f"Digite o {n}º número inteiro: "))
    nums.append(elemento)
    n = n + 1


mult = 1

for n in range(0, num):
    print(nums[n])
    mult = mult * nums[n]

print(mult)
"""
#Exercicio 3: Escreva um programa que retorne o maior e o menor número de uma lista.

"""
num = int(input("Escreva quantos números deseja trabalhar: \n"))

nums = []

n = 1
while n <= num:
    elemento = int(input(f"Digite o {n}º número inteiro: "))
    nums.append(elemento)
    n = n + 1

print(max(nums))
print(min(nums))
#Sem função


for n in range(0,num):
    for m in range(0, num):
        tmp = 0
        if nums[m] < nums[n]:
            tmp = nums[n]
            nums[n] = nums[m]
            nums[m] = tmp


print("Com a lista ordenada...\n\n")
print(nums)
print(f"O maior número é: {nums[0]}")
print(f"O menor número é: {nums[n]}")
"""

#Exercicio 4: Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com'
#Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )
#OBS: Não consegui fazer a ordenção

"""
palavra = input("Digite uma palavra: ")
palavra.upper()


lista = []
lista2 = []

for n in range(0, len(palavra)):
    aux = 0
    for m in range(0, len(palavra)):
        if(palavra[n] == palavra[m]):
            aux = aux + 1
            ajuda = (palavra[n], aux)
            lista.append(ajuda)


ordenado = dict(lista)

for i in sorted(ordenado, key = ordenado.get, reverse=True):
    ajuda = (i,ordenado[i])
    lista2.append(ajuda)

ordenado = dict(lista2)

print(ordenado)
"""

#Exercicio 5: Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres
#sejam iguais. (Exemplo de lista: ['abc','xyz','aba','1221']

"""
lista = []
ver = 0
resultado = 0
while ver == 0:
    palavra = input("Digite qualquer número ou letra: \n")
    if palavra == 'sair':
        ver = 1
        break
    print("\nDigite sair para obter os resultados!\n\n")
    palavra.upper()
    if(len(palavra) > 2):
        lista.append(palavra)
        if palavra[0] == palavra[len(palavra) - 1]:
            resultado = resultado + 1





print(f'A lista com uma string maior que 2 é: {lista}\n\n'
      f'O número de elementos em que primeiro e o último caracter são iguais é: {resultado}')

"""

#Exercicio 6: Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da
#tupla (Exemplo de lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Resultado esperado: [(2,1),(1,2),(2,3),(4,4),(2,5)]
"""
lista = []
tupla = ()
conf = 0
while conf == 0:
    a,b = input("Digite dois números no formato x,y(digite 0,0 para sair): ").split(",")
    a = int(a)
    b = int(b)

    if a != 0 and b != 0:
        lista.append(a)
        lista.append(b)
    else:
        conf = 1
        print("Finalizado")


for i in range(1, len(lista),2):
    for j in range(1, len(lista), 2):
        if (lista[j] > lista[i]):
            tmp = lista[i - 1]
            lista[i - 1] = lista[j - 1]
            lista[j - 1] = tmp
            tmp = lista[i]
            lista[i] = lista[j]
            lista[j] = tmp

tupla = tuple(lista)

print(f"Ordenado:  {lista}")

"""

#Exercicio 7: Escreva um programa que adicione uma chave (key) a um dicionário. (Exemplo dicionário(Dict): {0: 10, 1: 20}
#Resultado esperado: {0: 10, 1: 20, 2: 30} )

"""
lista = []
dicionario = {}
confirma = 0
aux = 0

while confirma == 0:
    num = int(input("Digite um número inteiro aleatório(0 para sair): "))
    if(num == 0):
        confirma = 1
        break
    lista.append(num)


for n in range(0, len(lista)):
    dicionario[n] = lista[n]
    aux = aux + lista[n]
    if n == len(lista) - 1:
        dicionario[n + 1] = aux


print(f'O dicionário criado é: {dicionario}')

"""
#Exercicio 8: Escreva um programa que concatene os dicionários abaixo e crie um novo.
#Exemplo dicionário(Dict):
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Resultado esperado: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
lista = []
newdict = {}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#Como eu já sei exatamente os valores que vou trabalhar, podemos fazer da seguinte maneira:

total = len(dic1) + len(dic2) + len(dic3)

for n in range(1, total + 1):
    if n < 3:
        valor = dic1[n]
    elif n < 5:
        valor = dic2[n]
    else:
        valor = dic3[n]

    lista.append(valor)


for n in range(0, len(lista)):
    newdict[n] = lista[n]

print(lista)
print(f"\nDicionário concatenado: {newdict}")
"""

#Exercicio 9 e 10:Escreva um programa que leia chaves e valores, crie um dicionário, e depois, verifique se uma chave
# informada existe em um dicionário. Escreva um programa que itere em um dicionário
# utilizando loops.

"""
lista = []
dicionario = {}
confirma = 0


while confirma == 0:
    chave = input("Digite uma chave para declarar um valor(digite enter para sair): ")
    if chave == '':
        confirma = 1
        break
    else:
        tipo = int(input("Qual valor deseja adicionar? \n1-Inteiro\n2-String:\n"))
        if tipo == 1:
            valor = int(input("Digite um valor inteiro:\n"))
            dicionario[chave] = valor
        elif tipo == 2:
            valor = input("Digite um valor de string: \n")
            dicionario[chave] = valor
        else:
            print("Valor inválido para o tipo escolhido!\n")



igual = input("\n\nDigite uma chave para conferir se ela existe em um dicionário: ")


if igual in dicionario:
    print(f"Existe! e o valor dela é {dicionario[igual]}")
else:
    print("Não existe!")
"""
#Exercicio 11,12 e 13: Escreva um programa que remova itens duplicados de uma lista

"""
listaex = ['1','3','5','7','9',2,4,6,8,10]

lista1 = []

lista2 = []

lista3 = [] #Lista vazia

lista4 = [] #Lista para copiar ou clonar uma lista

conf = 0
while conf == 0:
    menu = int(input("Deseja criar uma lista personalizada?\n1- Sim \n 2-Não\n"))
    if menu == 1:
        tam = int(input("Quantos elementos deseja adicionar à lista?\n"))
        for n in range(0, tam):
            elem = input(f"Digite aqui o {n + 1}ºelemento que deseja adicionar: \n")
            lista1.append(elem)
        print(f"------------------------------------------\n"
              f"Foi criado a lista personalizada:{lista1}\n"
              "--------------------------------------------")
        conf = 1
    elif menu == 2:
        for n in range(0, 10):
            x = random.randint(1,20)
            lista2.append(x)
        print(f"--------------------------------------------\n"
              f"Foi criado a lista:{lista2}\n"
              "--------------------------------------------")
        conf = 2
    else:
        print("Digite apenas uma das duas opções!\n\n")



#Copiando para uma lista
if conf == 2:
    for n in range(0, len(lista2)):
        lista4.append(lista2[n])
else:
    for n in range(0, len(lista1)):
        lista4.append(lista1[n])


print("Executando os seguintes procedimentos:\n")
print(f"---------------------------------------------------\nRemovendo itens duplicados de {lista4} \n"
        f"----------------------------------------------------\n")



tam = len(lista4)


aux = 0

l =[]
for i in lista4:
    if i not in l:
        l.append(i)



print("Itens removidos\n")
print(f"Nova lista: {l}")

print("Verificando se a lista está vazia:\n")

if l == []:
    print("Está vazia!\n\n\n")
else:
    print("Não está vazia\n\n\n")


print("Programa finalizado")

"""


















