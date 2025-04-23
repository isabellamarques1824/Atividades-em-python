"""
# código que eu consegui fazer
nota = float(input('Digite a sua nota:'))
while nota <0 or nota >10:
    nota  =float(input('Digite um valor válido:'))
print(f'A sua nota é {nota}')

#código aprimorado
nota = input('Digite a sua nota:')
while not nota.isnumeric():
    nota = input('Voce não digitou um número. tente novamente:')
nota = int(nota)
while nota <0 or nota >10:
    nota = input('Digite um valor válido:')
    nota = int(nota)
print(f'sua nota é {nota}')
"""

# tentativa 3
nota = input('Digite a sua nota:')
while (not nota.isnumeric()) or int(nota) <0 or int(nota) >10:
    nota = input('Digite um valor válido:')
print(f'sua nota é {nota}')




