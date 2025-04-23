nome = input('Digite seu nome:')
senha = input('Digite a sua senha:')
while senha == nome:
    senha = input('A sua senha não pode ser igual ao seu nome. tente novamente:')
print('pronto')