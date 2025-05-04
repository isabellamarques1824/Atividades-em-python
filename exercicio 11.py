
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

