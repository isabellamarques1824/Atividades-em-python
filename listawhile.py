# Exercício 1

while True:
    n = input('Diga um número:')
    if n.isnumeric():
        n = int(n)
        if n > 0 and n < 10:
            break

# Exercício 2


#nome
nome = input('Diga seu nome:')
while len(nome) < 3:
    nome = input('Diga seu nome:')

#idade
while True:
    idade = input('Diga um número:')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break

#salario
salario = input('Diga seu salário:')
while not salario.isnumeric():
    salario = input('Diga seu salario:')
salario = int(salario)

#sexo
sexo = input('diga f ou m ')
while sexo != 'f' and sexo != 'm':
    sexo = input('diga f ou m:')

#estado civil
ecivil = input('diga s, c, v ou d:')
while not(ecivil == 's' or ecivil == 'c' or ecivil == 'v' or ecivil == 'd'):
    ecivil = input('diga f ou m:')

#resultado

print(nome, idade, salario, sexo, ecivil )

# Exercício 3


a = 80
b = 200
t = 0
while a < b:
    a *=1.03
    b *=1.015
    t += 1
print(f'vai demorar {t} anos.')

# Exercício 4

contador = 1
soma = 0
while contador <= 5:
    n1 = input(f'Digite o {contador}° número:')
    while not n1.isnumeric():
        n1 = input('Digite um NÚMERO:')
    n1 = int(n1)
    soma = soma + n1
    contador = contador + 1
media = soma / 5
print(f'A media é {media} ')

# Exercício 5

a  = input('Diga o primeiro número:')
while not a.isnumeric():
    a = input('diga o primeiro numero:')
a = int(a)

b  = input('Diga o segundo número:')
while not b.isnumeric():
    b = input('diga o segundo numero:')
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a, end=' ')
    a += 1

# Exercício 6

usuario = input('diga seu nome de usuario:')
senha = input('DIGA A SUA SENHA:')
while usuario == senha:
    usuario = input('diga seu nome:')
    senha = input('diga sua senha: ')

# Exercício 7

num = 5
while num  <= 10:
    print(f'taboada do {num}')
    mult = 1
    while mult <= 10:
        print(f'{num}*{mult} = {num*mult}')
        mult += 1
    print( )
    num += 1

# Exercício 8

a = 1
b = 1
i = 2
n = input('quantos valores voce deseja ver:')
while not n.isnumeric():
    n = input('digite um valor válido:')
n = int(n)
print(a, b, end=' ')
while i < n:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i = i + 1

# Exercício 9

pares = 0
impares = 0
contador = 0
while contador <10:
    n = input(f'{contador + 1}° número:')
    while not n.isnumeric():
        n = input('Digite um NÚMERO:')
    n = int(n)
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    contador = contador + 1
print(f'tem {pares} pares e {impares} impares.')

# Exercício 10

n = input('digite um número:')
while not n.isnumeric():
    n = input('Digite um NÚMERO:')
n = int(n)
contador = n
fatorial = 1
while contador > 1:
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{n} fatorial é {fatorial}')

# Exercício 11

i = 2
n = input('digit um numero:')
while not n.isnumeric():
    n = input('Não é um número, tente novamente:')
n = int(n)
if n <=1:
    print('nao é primo')
elif n == 2:
    print('é primo')
else:
    while True:
        if n % i == 0:
            print('nao é primo')
            break
        elif i > n**(1/2):
            print('é primo')
            break
        i = i + 1

# Exercício 12

notas = input('Quantas notas voce vai enviar para o sistema?')
while not notas.isnumeric():
    notas = input('não é um número, tente novamente:')
notas = int(notas)
contador = 1
soma = 0
while contador <= notas:
    nota = input(f'Digite a {contador}° nota: ')
    while not nota.isnumeric():
        nota = input('não é um número, tente novamente:')
    nota = int(nota)
    soma = soma + nota
    contador = contador + 1
media = soma / notas
print(f'A media das notas é {media}')

# Exercício 13

salario = input('Digite o salario:')
while not salario.isnumeric():
    salario = input('não é um número, tente novamente:')
salario = float(salario)
ano = 1996
porcentagem = 0.015
while ano <= 2025:
    salario = salario + salario * porcentagem
    porcentagem = porcentagem * 2
    ano = ano + 1
print(f'O salário atual é R${salario:.2f}.')

# Exercício 14

contador = 1
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0
while True:
    n = input(f'digite o {contador}° número:')
    try:
        n = int(n)
    except ValueError:
        print('valor inválido!')
        continue
    if 0 <= n <= 25:
        intervalo_0_25 = intervalo_0_25 + 1
    elif 26 <= n <=50:
        intervalo_26_50 = intervalo_26_50 + 1
    elif 51 <= n <=75:
        intervalo_51_75 = intervalo_51_75 + 1
    elif 76 <= n <=100:
        intervalo_76_100 = intervalo_76_100 + 1
    elif n < 0:
        break
    contador = contador + 1

print(f'tem {intervalo_0_25} numeros no intervalo [0-25]\n'
      f'tem {intervalo_26_50} numeros no intervalo [26-50]\n'
      f'tem {intervalo_51_75} numeros no intervalo [51-75]\n'
      f'tem {intervalo_76_100} numeros no intervalo [76-100]')

# Exercício 15

eleitor1 = 'jose'
eleitor2 = 'ana'
eleitor3 = 'maria'
eleitor4 = 'francisco'

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
votobranco = 0
votonulo = 0

contador = 0
pessoas = input('Quantas pessoas vão votar?')
while not pessoas.isnumeric():
    pessoas = input('digite um valor válido:')
pessoas = int(pessoas)
while contador < pessoas:
    voto = input(f'1- {eleitor1}  \n'
                 f'2- {eleitor2} \n'
                 f'3- {eleitor3} \n'
                 f'4- {eleitor4} \n'
                 f'5- voto em branco\n'
                 f'Digite seu voto (USE O CODIGO REFERENTE AO SEU ELEITOR):')
    while not voto.isnumeric():
        voto = input('digite um valor válido: \n '
                     f'1- {eleitor1}  \n'
                     f'2- {eleitor2} \n'
                     f'3- {eleitor3} \n'
                     f'4- {eleitor4} \n'
                     f'5- branco\n'
                     f'Digite seu voto (USE O CODIGO REFERENTE AO SEU ELEITOR):')
    voto = int(voto)
    if voto == 1:
        voto1 = voto1 + 1
    elif voto == 2:
        voto2 = voto2 + 1
    elif voto == 3:
        voto3 = voto3 + 1
    elif voto == 4:
        voto4 = voto4 + 1
    elif voto == 5:
        votobranco = votobranco + 1
    else:
        votonulo = votonulo + 1
    contador = contador + 1

print(f'RESULTADO DA ELEIÇÃO:\n'
      f'VOTOS EM {eleitor1}: {voto1} votos.\n'
      f'VOTOS EM {eleitor2}: {voto2} votos.\n'
      f'VOTOS EM {eleitor3}: {voto3} votos.\n'
      f'VOTOS EM {eleitor4}: {voto4} votos.\n'
      f'VOTOS EM BRANCO: {votobranco} votos.\n'
      f'VOTOS NULOS: {votonulo} votos.\n'
      f'\n'
      f'A PORGENTAGEM DE VOTOS BRANCOS É DE {(votobranco / pessoas) * 100:.2f}\n'
      f'A PORGENTAGEM DE VOTOS NULOS É DE {(votonulo / pessoas) * 100:.2f}')




