#minha tentativa

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

#correção

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




