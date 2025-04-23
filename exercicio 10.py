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
