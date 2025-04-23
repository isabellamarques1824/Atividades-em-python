#nome
nome = input('digite seu nome:')
while len(nome) <=3 :
    nome = input('Seu nome deve conter mais que 3 letras. digite novamente:')

#idade
idade = input('digite sua idade:')
while (not idade.isnumeric()) or int(idade) <0 or int(idade) >150:
    idade = input('inválido. digite novamente:')
idade = int(idade)


#salario
salario = input('Digite o seu salário:')
while (not salario.isnumeric()) or float(salario) <=0:
    salario = input('Sálario inválido. digite novamente:')
salario = float(salario)

#genero
genero = input('digite o seu genero:("f" para feminino, ou "m" para masculino.)')
while genero != 'f' and genero != 'm':
    genero = input('inválido! digite "f" para feminino ou "m" para masculino')

#estado
estado = input('Digite o seu estado civil sendo\n'
               'Solteiro: s\n'
               'Casado: c\n'
               'Viuvo: v\n'
               'divorciado: d\n'
               'seu estado civil:')
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
    estado = input('valor inválido!!!\n'
                   'Digite o seu estado civil sendo\n'
                   'Solteiro: s\n'
                   'Casado: c\n'
                   'Viuvo: v\n'
                   'divorciado: d\n'
                   'seu estado civil:')

#resultado
print(f'Nome:{nome}\n'
      f'Idade:{idade}\n'
      f'Salario:{salario}\n'
      f'Genero:{genero}\n'
      f'Estado civil:{estado}')


