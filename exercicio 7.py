#minha tentativa

n = input('Digite um número:')
while not n.isnumeric():
    n = input('Digite um NÚMERO:')
n = int(n)
multiplicacao = 1
while multiplicacao <=10:
    resultado = n * multiplicacao
    print(f'{n} x {multiplicacao} = {resultado}')
    multiplicacao = multiplicacao + 1


#correção

num = 5
while num  <= 10:
    print(f'taboada do {num}')
    mult = 1
    while mult <= 10:
        print(f'{num}*{mult} = {num*mult}')
        mult += 1
    print( )
    num += 1


