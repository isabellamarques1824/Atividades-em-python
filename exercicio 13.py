"""
salario = 1000
ano = 1996
porcentagem = 0.015
while ano <= 2025:
    salario = salario + salario * porcentagem
    porcentagem = porcentagem * 2
    ano = ano + 1
print(f'O sálario atual é {salario:.2f}')
"""
salario = input('Digite o salario:')
while not salario.isnumeric():
    salario = input('não é um número, tente novamente:')
salario = float(salario)
ano = 1996
porcentagem = 0.015
while ano <= 2025:
    salario = salario + salario * porcentagem
    porcentagem = porcentagem * 2
    ano = ano + 1
print(f'O salário atual é R${salario:.2f}.')

