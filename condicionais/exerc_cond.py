#Exercicio 1: Faça um Programa que peça dois números e imprima o maior deles

"""

x, y = input("Digite dois números para descobrir qual o maior(x,y): ").split(",")

x = int(x)
y = int(y)

if x > y:
    print(f"O maior número é: {x} ")
elif x < y:
    print(f"O maior número é: {y}")
else:
    print("Os números são idênticos)
"""

#Exercicio 2: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

"""
x = int(input("Digite um valor inteiro para descobrir se é positivo ou negativo: "))

if x >= 0:
    print(f"O número {x} é positivo.")
else:
    print(f"O número {x} é negativo.")
"""

#Exercicio 3: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.


"""
str = input("Digite uma letra para determinar um sexo(F ou M): ").upper()

if str == "F":
    print("Feminino.")
elif str == "M":
    print("Masculino.")
else:
    print("Sexo inválido.")
"""

#Exercicio 4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""
str = input("Digite uma letra para verificar se é uma vogal ou consoante: ")


if len(str) == 1:
    str = str.upper()
    if str == "A" or str == "E" or str == "I" or str == "O" or str == "U":
        print(f"A letra {str} é uma vogal")
    else:
        print(f"A letra {str} é uma consoante")
else:
    print("Digite apenas uma letra")
"""

#Exercicio 5: Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada pelo aluno e apresentar:"
#A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#A mensagem “Reprovado”, se a média for menor do que sete;
#A mensagem “Aprovado com Distinção”, se a média for igual a dez.”
"""
x,y,media = input("Qual suas duas notas e sua média para descobrir se está aprovado(nota1,nota2,media)?\n").split(",")

x = float(x)
y = float(y)
media = float(media)

if (x + y) / 2 >= media:
    print("APROVADO":
elif (x + y) / 2 == 10.0:
    print("Aprovado com distinção")
else:
    print("REPROVADO")
"""

#Exercicio 6: Faça um Programa que leia três números e mostre o maior e o menor deles.

"""
x,y,z = input("Digite 3 números inteiros para obter o maior e o menor entre eles(x,y,z): ").split(",")

x = int(x)
y = int(y)
z = int(z)

if x > y and x > z:
    print(f"Maior número: {x}")
elif y > x and y > z:
    print(f"Maior número: {y}")
elif z > x and z > y:
    print(f"Maior número: {z}")
else:
    print("Valor inválido")


if x < y and x < z:
    print(f"Menor número: {x}")
elif y < x and y < z:
    print(f"Menor número: {y}")
elif z < x and z < y:
    print(f"Menor número: {z}")
else:
    print("Valor inválido")
"""

#Exercicio 7: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
"""
x,y,z = input("Digite 3 preços de produtos inteiros para saber qual vale a pena comprar(menor preço)(x,y,z): ").split(",")

x = float(x)
y = float(y)
z = float(z)

if x < y and x < z:
    print(f"Compre o produto com o preço: R${x}")
elif y < x and y < z:
    print(f"Compre o produto com o preço: R${y}")
elif z < x and z < y:
    print(f"Compre o produto com o preço: R${z}")
else:
    print("Valor inválido")
"""

#Exercicio 8: Faça um Programa que leia três números e mostre-os em ordem decrescente

"""
x = int(input("Digite um número de três para apresentar em ordem decrescente: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if z > y:
    tmp = z
    z = y
    y = tmp

if y > x:
    tmp = x
    x = y
    y = tmp

print(f"A ordem decrescente(maior pro menor) é: {x} {y} {z}")
"""

#Exercicio 9:Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou
# "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
str = input("Digite uma letra equivalente ao turno que você estuda: \n M-Matutino \n V-Vespertino \n N-Noturno\n")


if len(str) == 1:
    str = str.upper()
    if str == "M":
        print("Bom dia!")
    elif str == "V":
        print("Boa tarde!")
    elif str == "N":
        print("Boa noite!")
    else:
        print("Letra não encontrada, dentre as apresentadas")
else:
    print("Valor inválido, digite apenas 1 letra")
"""

#Exercicio 10:  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento

"""
sal = float(input("Informe o seu salário atual para calcular seus reajustes: \nR$"))

print(f"O valor do salário antes do reajuste é R${sal}")
if sal > 1500.00:
    print(f"O percentual do aumento é 5%\nO aumento será de {sal * 0.05}")
    sal = sal + (sal * 0.05)
    print(f"O novo salário é R${sal}")
elif 700 < sal < 1500:
    print(f"O percentual de aumento é 10%\nO aumento será de {sal * 0.10}")
    sal = sal + (sal * 0.10)
    print(f"O novo salário é R${sal}")
elif 280 < sal <= 700:
    print(f"O percentual de aumento é 15%\nO aumento será de {sal * 0.15}")
    sal = sal + (sal * 0.15)
    print(f"O novo salário é R${sal}")
elif  sal <= 280:
    print(f"O percentual de aumento é 20%\nO aumento será de {sal * 0.20}")
    sal = sal + (sal * 0.20)
    print(f"O novo salário é R${sal}")
else:
    print("Valor inválido")
"""
#Exercicio 11: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações

"""
val,hour= input("Digite aqui o valor de sua hora e a quantidade de horas trabalhadas no mês(valor,horas): ").split(",")

val = float(val)
hour = int(hour)

salB = val * hour


if salB <= 900:
    print(f"Salário Bruto:              {salB}\n"
          f"Imposto de renda:           {salB * 0}\n"
          f"INSS:                       {salB * 0.10}\n"
          f"FGTS:                       {salB * 0.11}\n"
          f"Total de descontos:         {(salB * 0.05) + (salB * 0.10)}\n"
          f"\nSalário Líquido:          {salB - ((salB * 0) + (salB * 0.10))}")
elif 900 < salB <= 1500:
    print(f"Salário Bruto:              {salB}\n"
          f"Imposto de renda:           {salB * 0.05}\n"
          f"INSS:                       {salB * 0.10}\n"
          f"FGTS:                       {salB * 0.11}\n"
          f"Total de descontos:         {(salB * 0.05) + (salB * 0.10)}\n"
          f"\nSalário Líquido:          {salB - ((salB * 0.05) + (salB * 0.10))}\n")
elif 1500 < salB <= 2500:
    print(f"Salário Bruto:              {salB}\n"
          f"Imposto de renda:           {salB * 0.10}\n"
          f"INSS:                       {salB * 0.10}\n"
          f"FGTS:                       {salB * 0.11}\n"
          f"Total de descontos:         {(salB * 0.10) + (salB * 0.10)}\n"
          f"\nSalário Líquido:          {salB - ((salB * 0.10) + (salB * 0.10))}\n")
elif salB > 2500:
    print(f"Salário Bruto:              {salB}\n"
          f"Imposto de renda:           {salB * 0.15}\n"
          f"INSS:                       {salB * 0.10}\n"
          f"FGTS:                       {salB * 0.11}\n"
          f"Total de descontos:         {(salB * 0.15) + (salB * 0.10)}\n\n"
          f"Salário Líquido:            {salB - ((salB * 0.15) + (salB * 0.10))}\n")
else:
    print("Valor inválido!")
"""

#Exercicio 12: Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

"""
day = int(input("Digite um número que corresponda a um dia da semana(1-7): "))

if 0 < day < 7:
    if day == 1:
        print("Domingo")
    elif day == 2:
        print("Segunda-feira")
    elif day == 3:
        print("Terça-feira")
    elif day == 4:
        print("Quarta-feira")
    elif day == 5:
        print("Quinta-feira")
    elif day == 6:
        print("Sexta-feira")
    elif day == 7:
        print("Sábado")
    else:
        print("Valor inválido")
else:
    print("Por favor, digite um número inteiro de 1 a 7.")
"""
#Exercicio 13: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um
# semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero
# E O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
n1,n2 = input("Digite duas notas parciais obtidas em uma disciplina ao longo do semestre(x,y): ").split(",")

n1 = float(n1)
n2 = float(n2)

media = (n1 + n2) / 2

if 9.0 <= media <= 10.0:
    print(f"NOTA 1                       : {n1}\n"
          f"NOTA 2                       : {n2}\n"
          f"MÉDIA                        : {media}\n"
          f"MÉDIA DE APROVEITAMENTO      : A\n"
          f"SITUAÇÃO:                    : APROVADO\n")
elif 7.5 <= media < 9.0:
    print(f"NOTA 1                       : {n1}\n"
          f"NOTA 2                       : {n2}\n"
          f"MÉDIA                        : {media}\n"
          f"MÉDIA DE APROVEITAMENTO      : B\n"
          f"SITUAÇÃO:                    : APROVADO\n")
elif 6.0 <= media < 7.5:
    print(f"NOTA 1                       : {n1}\n"
          f"NOTA 2                       : {n2}\n"
          f"MÉDIA                        : {media}\n"
          f"MÉDIA DE APROVEITAMENTO      : C\n"
          f"SITUAÇÃO:                    : APROVADO\n")
elif 4.0 <= media < 6.0:
    print(f"NOTA 1                       : {n1}\n"
          f"NOTA 2                       : {n2}\n"
          f"MÉDIA                        : {media}\n"
          f"MÉDIA DE APROVEITAMENTO      : D\n"
          f"SITUAÇÃO:                    : REPROVADO\n")
elif 0.0 <= media < 4.0:
    print(f"NOTA 1                       : {n1}\n"
          f"NOTA 2                       : {n2}\n"
          f"MÉDIA                        : {media}\n"
          f"MÉDIA DE APROVEITAMENTO      : E\n"
          f"SITUAÇÃO:                    : REPROVADO\n")
else:
    print("Por favor digite os valores corretos em unidades (0,1,2,3,4...10)")
"""

#Exercicio 14: Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

"""
x,y,z = input("Informe 3 lados de um triângulo(x,y,z): ").split(",")

x = float(x)
y = float(y)
z = float(z)

if z > y:
    tmp = z
    z = y
    y = tmp

if y > x:
    tmp = x
    x = y
    y = tmp

if x < (y + z) and y < (x + z) and z < (y + x):
    if x == y and x == z:
        print("Os lados formam um triângulo equilátero.")
    elif x == y or z ==y and x != z:
        print("Os lados formam um triângulo isósceles.")
    elif x != y and x != z and y != z:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Não é possível existir um triângulo a partir destes lados")
"""

#Exercicio 15: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c

"""
a,b,c = input("Informe os números de uma expressão de segundo grau para obter suas raízes(ax^^2,bx,c):  ").split(",")

a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - (4 * a * c)

x1 = ((-b) + (delta **0.5)) / 2 * a

x2 = ((-b) - (delta **0.5)) / 2 * a

if delta < 0:
    print("Não existem raízes reais para esta equação.")
elif delta == 0:
    print(f"Existe uma raíz real para solução desta equação: {x2}")
elif delta > 0:
    print("Existem duas raízes reais para solução desta equação: ")
    print(f"x1: {x1} \n x2: {x2}")
else:
    print("Erro!")
"""

#Exercicio 16: Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se
# este ano é ou não bissexto.

"""
x = int(input("Digite um determinado ano para descobrir se é ou não bissexto: "))

if x % 400 != 0 and x % 4 != 0:
    print(f"O ano {x} não é bissexto.")
else:
    print(f"O ano {x} é bissexto.")
"""

#Exercicio 17: Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

"""
d,m,y = input("Digite uma data no formato dd/mm/yy para descobrir se é uma data válida: ").split("/")

d = int(d)
m = int(m)
y = int(y)

print(d)

if 1 <= d <= 31 and 1 <= m <= 12:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 and d <= 31:
        print(f"A data {d}/{m}/{y} é válido.")
    elif m == 2:
        if d < 29 and (y % 4 != 0 or y % 400 != 0):
            print(f"A data {d}/{m}/{y} é válido.")
        elif d < 30 and (y % 4 == 0 or y % 400 == 0):
            print(f"A data {d}/{m}/{y} é válido.")
        else:
            print(f"A data {d}/{m}/{y} é inválid.")
    elif d < 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        print(f"A data {d}/{m}/{y} é válido.")
    else:
        print(f"A data {d}/{m}/{y} é inválido.")
else:
    print(f"A data {d}/{m}/{y} é inválida.")
"""
#Exercicio 18: Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
# unidades do mesmo.
"""
x = int(input("Informe um número inteiro menor que 1000 para descobrir a quantidade de centenas,dezenas e unidades: "))

if 0 <= x < 1000:
    aux = int(x / 100)
    print(f"Centenas : {(aux)}\n")
    x = x - (100 * aux)
    aux = int(x / 10)
    print(f"Dezenas : {int(aux)}\n")
    x = x - (10 * aux)
    print(f"Unidades: {int(x)}")
else:
    print("Por favor, digite um número inteiro menor que 1000 e maior ou igual a 0")
"""

x,y,z = input("Digite tres números: ").split("/")

x = int(x)
y = int(y)
z = int(z)



if z > x and z < y:
    print("A")

if x == y:
    print("B")

if x != y:
    print("C")

if x != y and y < 0:
    print("D")
    if z < 0:
        w = "-"
    else:
        w = "+"

print(w)




