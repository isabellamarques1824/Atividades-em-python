notas = input('Quantas notas voce vai enviar para o sistema?')
while not notas.isnumeric():
    notas = input('não é um número, tente novamente:')
notas = int(notas)
contador = 1
soma = 0
while contador <= notas:
    nota = input(f'Digite a {contador}° nota: ')
    while not nota.isnumeric():
        nota = input('não é um número, tente novamente:')
    nota = int(nota)
    soma = soma + nota
    contador = contador + 1
media = soma / notas
print(f'A media das notas é {media}')


