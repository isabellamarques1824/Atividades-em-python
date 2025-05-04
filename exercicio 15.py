
# exercicio 15


eleitor1 = 'jose'
eleitor2 = 'ana'
eleitor3 = 'maria'
eleitor4 = 'francisco'

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
votobranco = 0
votonulo = 0

contador = 0
pessoas = input('Quantas pessoas vão votar?')
while not pessoas.isnumeric():
    pessoas = input('digite um valor válido:')
pessoas = int(pessoas)
while contador < pessoas:
    voto = input(f'1- {eleitor1}  \n'
                 f'2- {eleitor2} \n'
                 f'3- {eleitor3} \n'
                 f'4- {eleitor4} \n'
                 f'5- voto em branco\n'
                 f'Digite seu voto (USE O CODIGO REFERENTE AO SEU ELEITOR):')
    while not voto.isnumeric():
        voto = input('digite um valor válido: \n '
                     f'1- {eleitor1}  \n'
                     f'2- {eleitor2} \n'
                     f'3- {eleitor3} \n'
                     f'4- {eleitor4} \n'
                     f'5- branco\n'
                     f'Digite seu voto (USE O CODIGO REFERENTE AO SEU ELEITOR):')
    voto = int(voto)
    if voto == 1:
        voto1 = voto1 + 1
    elif voto == 2:
        voto2 = voto2 + 1
    elif voto == 3:
        voto3 = voto3 + 1
    elif voto == 4:
        voto4 = voto4 + 1
    elif voto == 5:
        votobranco = votobranco + 1
    else:
        votonulo = votonulo + 1
    contador = contador + 1

print(f'RESULTADO DA ELEIÇÃO:\n'
      f'VOTOS EM {eleitor1}: {voto1} votos.\n'
      f'VOTOS EM {eleitor2}: {voto2} votos.\n'
      f'VOTOS EM {eleitor3}: {voto3} votos.\n'
      f'VOTOS EM {eleitor4}: {voto4} votos.\n'
      f'VOTOS EM BRANCO: {votobranco} votos.\n'
      f'VOTOS NULOS: {votonulo} votos.\n'
      f'\n'
      f'A PORGENTAGEM DE VOTOS BRANCOS É DE {(votobranco / pessoas) * 100:.2f}\n'
      f'A PORGENTAGEM DE VOTOS NULOS É DE {(votonulo / pessoas) * 100:.2f}')

