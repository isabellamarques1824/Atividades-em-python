
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
