# minha tentativa

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

