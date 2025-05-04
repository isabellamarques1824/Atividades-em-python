
#exercicio 14


contador = 1
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0
while True:
    n = input(f'digite o {contador}° número:')
    try:
        n = int(n)
    except ValueError:
        print('valor inválido!')
        continue
    if 0 <= n <= 25:
        intervalo_0_25 = intervalo_0_25 + 1
    elif 26 <= n <=50:
        intervalo_26_50 = intervalo_26_50 + 1
    elif 51 <= n <=75:
        intervalo_51_75 = intervalo_51_75 + 1
    elif 76 <= n <=100:
        intervalo_76_100 = intervalo_76_100 + 1
    elif n < 0:
        break
    contador = contador + 1

print(f'tem {intervalo_0_25} numeros no intervalo [0-25]\n'
      f'tem {intervalo_26_50} numeros no intervalo [26-50]\n'
      f'tem {intervalo_51_75} numeros no intervalo [51-75]\n'
      f'tem {intervalo_76_100} numeros no intervalo [76-100]')
