n = input('Digite um número:')
while not n.isnumeric():
    n = input('não é um número, tente novamente:')
n = int(n)
