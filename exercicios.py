

# exercicio 1

while True:
    nota = input('Digite sua nota:')
    if nota.isnumeric():
        nota = int(nota)
        if 0 <= nota <= 10:
            print(f'deu certo. sua nota é {nota}')
            break
        else:
            print('valor invalido, tente novamente')
    else:
        print('não é um número. tente novamente.')


#exercicio 2

# nome

nome = input('digite seu nome:')
while len(nome) < 3:
    nome = input('digite seu nome corretamente:')


# idade

while True:
    idade = input('digite sua idade:')
    if idade.isnumeric():
        idade = int(idade)
        if 0 < idade < 150:
            break
        else:
            print('idade inválida, tente novamente.')
    else:
        print('não é um número, tente novamente.')


# salario


while True:
    salario = input('digite seu sálario:')
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break
        else:
            print('inválida, tente novamente.')
    else:
        print('não é um número, tente novamente.')


# sexo

sexo = input('qual seu genero? feminino(f) ou masculino(m):')
while sexo != 'f' and sexo != 'm':
    sexo = input('digite um valor válido:')



# estado civil

estado = input('qual é o seu estado civil?\n'
               'solteiro: s, casado: c, viuvo: v, divorciado: d ')
while estado != 's'  and estado != 'c' and estado != 'v' and estado != 'd':
    estado = input('digite um valor valido:\n'
                   'solteiro: s, casado: c, viuvo: v, divorciado: d')


print(nome, idade, salario, sexo, estado)


# exercicio 3

a = 80
b = 200
ano = 0

while a < b:
    a = a * 1.03
    b = b * 1.015
    ano += 1
print(f'vai demorar {ano} anos para A passar de B')

# exercicio 4

contador = 1
soma = 0
while contador <= 5:
    n = input(f'digite o {contador}° número:')
    while not n.isnumeric():
        n = input('digite um numero válido:')
    n = int(n)
    soma = soma + n
    contador = contador + 1
media = soma / 5
print(f'a soma é {soma} e a media é {media}')



#exercicio 5

n1 = input('Digite o primeiro número:')
while not n1.isnumeric():
    n1 = input('digite um valor válido:')
n1 = int(n1)
n2 = input('Digite o segundo número:')
while not n2.isnumeric():
    n2 = input('digite um valor válido:')
n2 = int(n2)

if n1 > n2:
    n = n1
    n1 = n2
    n2 = n
while n1 <=n2:
    print(n1)
    n1 += 1




#exercicio 6


while True:
    nome = input('Digite o seu nome:')
    senha = input('Digite sua senha:')
    if senha != nome:
        break
    else:
        print('a sua senha não pode ser igual ao seu nome, tente novamente.')





# exercicio 7

n = input('digite um numero:')
mult = 1
while not n.isnumeric():
    n = input('digite um valor válido:')
n = int(n)
while mult <10:
    print(f'{n} x {mult} = {n * mult}')
    mult = mult + 1


#exercicio 8

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


# exercicio 9

contador = 1
pares = 0
impares = 0
while contador <= 10:
    n = input(f'digite o {contador}° número:')
    while not n.isnumeric():
        n = input('digite um valor válido:')
    n = int(n)
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    contador = contador + 1

print(f'tem {pares} numeros pares e {impares} numeros impares.')

# exercicio 10



n = input(f'digite um número:')
while not n.isnumeric():
    n = input('digite um valor válido:')
n = int(n)
contador = n
fatorial = 1
while contador > 1:
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{n} fatorial é {fatorial}')





#exercicio 11


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


#exercicio 12


i = 1
soma = 0
notas = input('quantas notas voce vai inserir no programa?')
while not notas.isnumeric():
    notas = input(f'digite um valor valido:')
notas = int(notas)
while i <= notas:
    nota = input(f'digite a {i}° nota: ')
    while not nota.isnumeric():
        nota = input(f'digite um valor valido:')
    nota = int(nota)
    soma = soma + nota
    i = i + 1
media = soma / notas
print(f'a media é {media}')




#exercicio 13

salario = input('digite seu salario')
while not salario.isnumeric():
    salario = input(f'digite um valor valido:')
salario = int(salario)
aumento = 1.015
salarionovo = 0
ano = 1995
while ano < 2000:
    salario = salario * aumento
    aumento = aumento * 2
    ano = ano + 1
print(f'voce vai receber {salario} em {ano}')



#exercicio 14


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


# exercicio 15


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








