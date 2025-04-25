#minha tentativa

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


#correção

#nome
nome = input('Diga seu nome:')
while len(nome) < 3:
    nome = input('Diga seu nome:')

#idade
while True:
    idade = input('Diga um número:')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break

#salario
salario = input('Diga seu salário:')
while not salario.isnumeric():
    salario = input('Diga seu salario:')
salario = int(salario)

#sexo
sexo = input('diga f ou m ')
while sexo != 'f' and sexo != 'm':
    sexo = input('diga f ou m:')

#estado civil
ecivil = input('diga s, c, v ou d:')
while not(ecivil == 's' or ecivil == 'c' or ecivil == 'v' or ecivil == 'd'):
    ecivil = input('diga f ou m:')

#resultado

print(nome, idade, salario, sexo, ecivil )


