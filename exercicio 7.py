n = input('Digite um número:')
while not n.isnumeric():
    n = input('Digite um NÚMERO:')
n = int(n)
multiplicacao = 1
while multiplicacao <=10:
    resultado = n * multiplicacao
    print(f'{n} x {multiplicacao} = {resultado}')
    multiplicacao = multiplicacao + 1

