# Exercício 1: Escreva um programa que execute uma função que
# encontre o maior número de uma lista passada por
# parâmetro.

""""
def maior(lista):
    m = 0
    for x in range(0, len(lista)):
        for y in range(0, len(lista)):
            if lista[x] > lista[y]:
                tmp = lista[x]
                lista[x] = lista[y]
                lista[y] = tmp


    return lista[0]



num = int(input("Escreva quantos números deseja adicionar: \n"))

nums = []

for x in range(0,num):
    n = int(input("Digite um número inteiro para adicionar para um número inteiro:\n"))
    nums.append(n)


print(f"O maior número da lista {nums} que foram citados é {maior(nums)}")

"""

# Exercicio 2: Escreva um programa que execute uma função que
# some todos os itens de uma lista passada por
# parâmetro

"""
def soma(lista):
    m = 0
    for x in range(0, len(lista)):
        m = lista[x] + m

    return m




num = int(input("Escreva quantos números deseja adicionar: \n"))

nums = []

for x in range(0,num):
    n = int(input("Digite um número inteiro para adicionar em uma lista: \n"))
    nums.append(n)


print(f"A soma dos números da lista {nums} que foram citados é {soma(nums)}")
"""

# Exercicio 3: Escreva um programa que execute uma função que
# multiplique todos os números de uma lista passada por
# parâmetro


"""
def mult(lista):
    m = 1
    for x in range(0, len(lista)):
        m = m * lista[x]

    return m




num = int(input("Escreva quantos números deseja adicionar: \n"))

nums = []

for x in range(0,num):
    n = int(input("Digite um número inteiro para adicionar em uma lista: \n"))
    nums.append(n)

print(f"A multiplicação dos números da lista {nums} que foram citados é {mult(nums)}")
"""

# Exercicio 4:Escreva um programa que execute uma função que
# retorne o inverso de uma string passada por parâmetro.

"""
def inv(palavra):
    s = []
    x = len(palavra)
    while x > 0:
        s += palavra[x - 1]
        x = x - 1
    s = str(s)
    
    aux = ""
    for x in range(0, len(s)):
        if s[x] != ']' and s[x] != '[' and s[x] != ',':
            aux =aux + s[x]


    return aux


pal = input("Escreva uma palavra para receber seu valor inverso \n")

print(f"A palavra mencionada foi {pal} e sua forma inversa é: {inv(pal)}")
"""

# Exercicio 5:Escreva um programa que execute uma função que
# calcule o fatorial de um número passado por parâmetro.

"""
def fatorial(num):
    if num == 0:
        return 1

    if(num != 1):
        return num * fatorial(num - 1)
    else:
        return 1


numero = int(input("Digite um número para descobrir seu fatorial:\n"))

print(f"O fatorial de {numero} é: {fatorial(numero)}")
"""

# Exercicio 6:Escreva um programa que execute uma função que
# conte o número de letras maiúsculas e minúsculas de
# um texto e que ao final, chame outra função para
# imprimir o resultado.

"""
def print_result(maior, menor):
    print(f"O número de letras maiúsculas é: {maior}\n"
          f"O número de letras minúsculas é: {menor}\n")


def conta_letra(palavra):
    mai = 0
    men = 0
    for x in range(0, len(palavra)):

        if 65 <= ord(palavra[x]) <= 90:
            mai = mai + 1
        elif 97 <= ord(palavra[x]) <= 122:
            men = men + 1

    return mai,men


palavra = input("Qual palavra deseja escrever:\n")

x,y = conta_letra(palavra)
print_result(x,y)
"""
"""
#Exercicio 7:
#Escreva um programa Python que execute uma string
#que contenha um código Python.

def cod():
    print("a = 1 + 5\n"
           "print(a)")


cod()
"""

# Exercicio 8:Escreva um programa que execute uma função que
# receba um número informado no console como
# parâmetro e verifique se o número informado é primo ou
# não
"""

def primo(num):
    if num == 1 or num == 0:
        return 0
    else:
        resultado = 0
        for x in range(2, num - 1):
            if num % x == 0:
                resultado = resultado + 1
                print(resultado)
        if resultado >= 1:
            return 1

        else:
            return 0









def rec_num():
    numero = int(input("Digite um número inteiro para descobrir se é primo ou não: \n"))

    if(primo(numero) == 0):
        print(f"O número {numero} é primo!\n")

    else:
        print(f"O número {numero} não é primo!\n")


rec_num()
"""

# Exercicio 9:Escreva um programa que execute uma função que
# valide se o número informado é um número perfeito ou
# não.
"""
def perfeito(numero):
    total = 0
    for x in range(1,numero):
        if (numero % x == 0):
            total = total + x

    if total == numero:
        return "É perfeito!"
    else:
        return "Não é perfeito"

num = int(input("Digite um número para descobrir se ele é perfeito ou não: \n"))
print(perfeito(num))
"""


# Exercicio 10:Escreva uma função que imprima as primeiras n linhas
# do triângulo de pascal

def posi(i, j):
    if j == 0 or j == i:
        return 1
    else:
        return int(posi(i - 1, j - 1)) + int(posi(i - 1, j))


def pascal(linhas):
    linhas = linhas + 1
    tria = []

    for linha in range(linhas):
        val_linha = []

        for coluna in range(linha + 1):
            val_linha.append(posi(linha, coluna))

        tria.append(val_linha)

    return tria

tam = int(input("Digite qual o tamanho das linhas do triângulo de pascal que deseja escolher:\n"))
print(pascal(tam))



