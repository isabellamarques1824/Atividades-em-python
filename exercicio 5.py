#minha tentativa

n1 = input('Digite o primeiro número inteiro:')
while (not n1.isnumeric()) or n1 == float:
    n1 = input('Digite um NÚMERO INTEIRO:')
n1 = int(n1)
n2 = input('Digite o segundo número inteiro:')
while (not n2.isnumeric()) or n2 == float:
    n2 = input('Digite um NÚMERO INTEIRO:')
n2 = int(n2)
if n1 > n2:
    n2 = n1
    n = n1 + 1
else:
    n = n1 + 1

while n < n2 or n < n1:
    print(n)
    n = n + 1


#correção

a  = input('Diga o primeiro número:')
while not a.isnumeric():
    a = input('diga o primeiro numero:')
a = int(a)

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





