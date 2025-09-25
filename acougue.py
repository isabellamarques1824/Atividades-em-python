import pandas as pd
import requests
acougue = {
    'carne': ['patinho', 'coxão mole', 'fraldinha', 'maminha', 'picanha', 'linguiça'],
    'R$/kg': [35.90,49.90,39.90,80.00,45,90.15],
    'estoque': [10,50,30,15,20,100],
    'validade': ['4','7', '5', '9','20','50']
}

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes}\n->")
    while not opcao in lista_opcoes:
        print("Invalido")
        opcao = input(f"{msg}\n{opcoes}\n->")
    return opcao

def verificanum(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def cria_indice():
    indices_dic = {acougue['carne'][i] : i for i in range(len((acougue['carne'])))}
    return indices_dic

def cadastrar():
    global indices
    for key in acougue.keys():
        info = input(f"Diga o novo {key}:")
        acougue[key].append(info)
    indices = cria_indice()
    return

def remover():
    global indices
    escolha = forca_opcao("qual item será removido: ", acougue['carne'])
    indice_escolha = indices[escolha]
    for key in acougue.keys():
        acougue[key].pop(indice_escolha)
    indices = cria_indice()
    return

def atualizar():
    item = forca_opcao('Qual item você deseja atualizar: ', acougue['carne'])
    indice_item = indices[item]
    for key in acougue.keys():
        escolha = forca_opcao(f"Você deseja atualizar o {key}?",['sim','não'])
        if  escolha == 'sim':
            info = input(f'diga o novo {key}: ')
            acougue[key][indice_item] = info
    return

def comprar():
    item = forca_opcao("qual item você deseja comprar? ", acougue['carne'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f'{key}: {acougue[key][indice_item]}')
    continuar = forca_opcao(f'Você quer levar {item}?', ['sim', 'não'])
    if continuar == 'não':
        return
    qnt = verificanum(f"quantos kg de {item}")
    if qnt <= acougue['estoque'][indice_item]:
        acougue['estoque'][indice_item] -= qnt
        carrinho['valor total'] += qnt*acougue['R$/kg'][indice_item]
        if item not  in carrinho['itens'].keys():
            carrinho['itens'][item] = qnt
        else:
            carrinho['itens'][item] += qnt
    else:
        print(f'Só há {acougue['estoque'][indice_item]} kg no estoque! ')
    return

print(pd.DataFrame(acougue))
indices = cria_indice()

carrinho = {
    'endereço': {
        'rua': '',
        'bairro': '',
        'N°': '',
        'cep': ''},
    'itens': {},
    'valor total': 0

}
def cadastro_endereco():
    while True:
        cep = input('Diga o seu cep: ')
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if endereco.status_code == 200:
            carrinho['endereço'] = endereco.json()
            carrinho['endereço']['complemento'] = input('complemento: ')
            break
        else:
            print('cep inválido!')
    return

while True:
    print('BEM VINDO AP AÇOUGUE AGNELLO! 👌👌👌👌😘💕🍖🍖')
    usuario = forca_opcao('você é cliente ou funcionário?', ['cliente', 'funcionário'])
    if usuario == 'funcionário':
        operacao = forca_opcao('Digite um setor: ', ['cadastrar', 'remover', 'atualizar'])
        if operacao =='cadastrar':
            cadastrar()
        elif operacao == 'remover':
            remover()
        else:
            atualizar()
        continuar = forca_opcao('você deseja realizar outra operação?', ['sim', 'não'])
        if continuar == 'não':
            break
    else:
        while True:
            comprar()
            encerrar = forca_opcao('Encerrar a comprar ou ver mais itens?', ['encerrar', 'continuar'])
            if encerrar == 'encerrar':
                print(carrinho)
                break