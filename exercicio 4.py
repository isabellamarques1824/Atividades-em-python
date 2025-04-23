"""
n1 = input('Digite o primeiro número:')
while not n1.isnumeric():
    n1 = input('Digite um NÚMERO:')
n1 = int(n1)
n2 = input('Digite o segundo número:')
while not n2.isnumeric():
    n2 = input('Digite um NÚMERO:')
n2 = int(n2)
n3 = input('Digite o terceiro número:')
while not n3.isnumeric():
    n3= input('Digite um NÚMERO:')
n3 = int(n3)
n4 = input('Digite o quarto número:')
while not n4.isnumeric():
    n4 = input('Digite um NÚMERO:')
n4 = int(n4)
n5 = input('Digite o quinto número:')
while not n5.isnumeric():
    n5 = input('Digite um NÚMERO:')
n5 = int(n5)
soma = n1 + n2 + n3 + n4 + n5
media = (n1 + n2 + n3 + n4 + n5)/5
print(f'A soma entre eles é {soma}, e a média é {media}')
"""
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



