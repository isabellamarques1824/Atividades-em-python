#exercicio 1

while True:
    n = input('Diga um número:')
    if n.isnumeric():
        n = int(n)
        if n > 0 and n < 10:
            break


#exercicio 2

nome = input('Diga seu nome:')
while len(nome) < 3:
    nome = input('Diga seu nome:')

while True:
    idade = input('Diga um número:')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break

salario = input('Diga seu salário:')
while not salario.isnumeric():
    salario = input('Diga seu salario:')
salario = int(salario)

sexo = input('diga f ou m ')
while sexo != 'f' and sexo != 'm':
    sexo = input('diga f ou m:')

ecivil = input('diga s, c, v ou d:')
while not(ecivil == 's' or ecivil == 'c' or ecivil == 'v' or ecivil == 'd'):
    ecivil = input('diga f ou m:')


#exrcicio 3

a = 80
b = 200
t = 0
while a < b:
    a *=1.03
    b *=1.015
    t += 1
print(t)

#exercicio 4

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

# exercicio 5

a  = input('Diga o primeiro número:')
while not a.isnumeric():
    a = input('diga o primeiro numero:')
a = int(b)

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

# exercicio 6

senha = '1234'
password = input('diga sua senha:')
tentativa = 1
while senha != password and tentativa <3:
    print('senha invalida')
    password = input('diga sua senha:')
    tentativa += 1

if password == senha:
    print('acesso liberado')

else:
    print('sai hacker')

usuario = input('diga seu nome de usuario:')
senha = input('DIGA A SUA SENHA:')
while usuario == senha:
    usuario = input('diga seu nome:')
    senha = input('diga sua senha: ')


# exercicio 7

num = 5
while num  <= 10:
    print(f'taboada do {num}')
    mult = 1
    while mult <= 10:
        print(f'{num}*{mult} = {num*mult}')
        mult += 1
    print( )
    num += 1


#exercicio 8

a = 1
b = 1
print(a,b,end='')
i = 0

while i < 10:
    c  = a + b
    print(c,end = '')
    a = b
    b = c
    i += 1

#exercicio 9

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

#exercicio 10

i = 1
fatorial = 1
while i < 5:
    i += 1
   fatorial *= i
print(fatorial)


i = 1
fatorial = 1
num = 5
produto = f'{num}! = '
while i < num:
    produto += f'{i}*'
    i += 1
   fatorial *= i
produto += f'1 = {fatorial}'
print(produto)

#exercicio 11

i = 0
soma = 0
while i < 10:
    i += 1
    soma += i
print(soma)

#exercicio 12

num = 7
i = 2
while True:
    print(f'{num}%{i} = {num%i}')
    if num  %i == 0:
        print('n é primo')
        break
    elif i >= num**(1/2):
        print('é primo')
        break
    i += 1



 #exercicio 13

salario = 1000
ano = 1995
taxainicial = 0.015
while ano <2000:
    taxa = 1 + taxainicial
    taxainicial *= 2
    salario *= taxa
    ano +=1
print(salario)

#exercicio  14
















