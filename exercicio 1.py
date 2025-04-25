#minha tentativa

nota = input('Digite a sua nota:')
while (not nota.isnumeric()) or int(nota) <0 or int(nota) >10:
    nota = input('Digite um valor válido:')
print(f'sua nota é {nota}')

#correção

while True:
    n = input('Diga um número:')
    if n.isnumeric():
        n = int(n)
        if n > 0 and n < 10:
            break




