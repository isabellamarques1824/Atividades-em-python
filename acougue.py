import pandas as pd
import requests
from numba import typeof

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

#essa parte tá incompleta/ com algum erro
def printa_dic(dic,num=0):
    for key in dic.keys():
        if type(dic[key]) is dict:
            print(key)
            printa_dic(dic[key],num+1)
        else:
            print(f'{num*''}')

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
        if key == 'R$/kg':
            while True:
                try:
                    info = float(input(f"Diga o novo {key}: "))
                except ValueError:
                    print('Valor inválido. Precisa ser float: a virgula é ponto - 1,5 -> 1.5')
                else:
                    break
        elif key == 'estoque':
            info = verificanum(f'Diga o novo {key}: ')
        else:
            info = input(f"Diga o novo {key}: ")
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

def confirmar_compra():
    print('Essas são as informações da sua compra: ')
    printa_dic(carrinho)
    alterar = forca_opcao('Deseja remover algum item?', ['s','n'])
    if alterar == 's':
        item = forca_opcao('qual item vc vai remover? ', carrinho['itens'].keys())
        indice = indices[item]
        qnt = verificanum(f'quantos kg de {item} serão removidos?')
        if qnt <= carrinho['itens'][item]:
            carrinho['itens'][item] -= qnt
            carrinho['valor total'] -= qnt*acougue['R$/kg'][indice]
        else:
            print(f'não é possivel remover esse tanto pois só há {carrinho['itens'][item]}kg')
        confirmar_compra()
    return
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


acoes  = {
    'cadastrar': cadastrar,
    'remover': remover,
    'atualizar': atualizar,
    'sair': exit
}

print('BEM VINDO AP AÇOUGUE AGNELLO! 👌👌👌👌😘💕🍖🍖')
usuario = forca_opcao('você é cliente ou funcionário?', ['cliente', 'funcionário'])
if usuario == 'cliente':
    cadastro_endereco()

while True:
    if usuario == 'funcionário':
        operacao = forca_opcao('Digite um setor: ', acoes.keys())
        acoes[operacao]()
    else:
        while True:
            comprar()
            encerrar = forca_opcao('Encerrar a comprar ou ver mais itens?', ['encerrar', 'continuar'])
            if encerrar == 'encerrar':
                printa_dic(carrinho)
                break


# esse código não está completo