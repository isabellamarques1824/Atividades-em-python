import matplotlib.pyplot as plt


def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][[{j}] = {matriz[i][j]}')
    return


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    print()
    return


def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(i)
        matriz.append(lista)
    return matriz


def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return


def diagonal_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                matriz[i][j] = 1
    return


def diagonal_boa(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return


def diagonalaocontrario(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                matriz[i][j] = 1
    return


def conradiagonal(matriz):
    for i in range(len(matriz)):
        j = len(matriz) - i - 1
        matriz[i][j] = 1


def xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i % 2 == j % 2:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    return


def coresdiferentesdiagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > i:
                matriz[i][j] = 1
            elif j < i:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 0.6


def superiorcor_bom(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz[0])):
            if j > i:
                matriz[i][j] = 1


def transpostaruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > i:
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux
    return


def transpostaboa(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return