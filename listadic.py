def forcaopcao(msg, lista_opcoes):
    msg += '\n' + '\n'.join(lista_opcoes) + '\n-->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print('erro!')
        opcao = input(msg)
    return opcao

def achaindice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def indicemaior(lista):
    indicemaior = 0
    for i in range(len(lista)):
        if lista[i] > lista[indicemaior]:
            indicemaior = i
    return indicemaior

def indicemenor(lista):
    indicemenor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indicemenor]:
            indicemenor = i
    return indicemenor

# Exercício 1

saudacoes = {"oi": "hello", "tchau": "tchau"}

resposta =  input("Diga oi ou tchau: ")
print(saudacoes[resposta])

# Exercício 2

carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno' ],
    'portas': [4,2,6,2],
    'preço': [1000,200,300,100],
    'ano de fabrição': [2014, 2018, 1970, 2005]
}

carro = forcaopcao("qual carro vc quer?", carros['nomes'])
indice = achaindice(carros['nomes'], carro)

for key in carros.keys():
    print(carros[key][indice])


# Exercício 3

carrocaro = indicemaior(carros['preço'])
for key in carros.keys():
    print(f'{key}: {carros[key][carrocaro]}')


# Exercício 4

carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno' ],
    'portas': [4,2,6,2],
    'preço': [1000,200,300,100],
    'ano de fabrição': [2014, 2018, 1970, 2005]
}

carromenor = indicemenor(carros['preço'])
for key in carros.keys():
    print(f'{key}: {carros[key][carromenor]}')


# Exercício 5


def cadastrar(carros):
    for key in carros.keys():
        info = input(f'diga o novo {key}: ')
        carros[key].append(info)
    return


# Exercício 6

remover = forcaopcao("qual carro vc quer remover? ", carros['nomes'])
indiceremover = achaindice(carros['nomes'], remover)
for key in carros.keys():
    carros[key].pop(indiceremover)
print(carros)

# Exercício 7

frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o  desconstantinopolitanizar, um bom desconstantinopolitanizador será.'
frase = frase.lower()
for char in ',.;:?!':
    frase = frase.replace(char, '')
print(frase)
palavras = frase.split(' ')
contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 1
    else:
        contador[palavra] += 1


numeros = {
    'zero': '0',
    'dois': '2',
    'cinco': '5'
}

frase = 'EU TENhO AULA  na sala cinco zero dois '


#desisti de completar dps eu arrumo bonitinho

# Exercício 9

dic1 = {'a': 10, 'b': 20, 'c': 30}
dic2 = {'b': 10, 'c': 20, 'd': 30}

chaves = []

for key1 in dic2.keys():
    chaves.append(key1)
print(chaves)

chaves2 = []
for key1 in dic1.keys():
    if key1 in dic2.keys():
        chaves2.append(key1)
print(chaves2)

# Exercício 10

disjuncao = []
for key2 in dic1.keys():
    if key2 not in dic2.keys():
        disjuncao.append(key2)
    print(disjuncao)
