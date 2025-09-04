import matplotlib.pyplot as plt

def plotar_matriz(matriz):
    plt.imshow(matriz, 'hot')
    plt.colorbar()
    plt.show()
    return

#Exercício 1 - printar matriz

def printar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

matriz = [[1,2],[3,4],[5,6],[7,8]]
printar_matriz(matriz)

#Exercício 2 - Criar matriz preenchida com 0

def criar_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linhas = []
        for j in range(colunas):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

matriz_de0 = criar_matriz(10,10)
printar_matriz(matriz_de0)

#Exercício 3 - Diagonal

def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return

matriz_diagonal = criar_matriz(10,10)
diagonal(matriz_diagonal)
printar_matriz(matriz_diagonal)

#Exercício 4 - Contra Diagonal

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        j = len(matriz) - 1 - i
        matriz[i][j] = 1
    return

matriz_contra_diagonal = criar_matriz(10,10)
contra_diagonal(matriz_contra_diagonal)
printar_matriz(matriz_contra_diagonal)

#Exercício 5 - Acima da diagonal vale 1, abaixo vale 0

def acima_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz[0])):
            matriz[i][j] = 1
    return

matriz_acima_diagonal = criar_matriz(10,10)
acima_diagonal(matriz_acima_diagonal)
printar_matriz(matriz_acima_diagonal)

#Exercício 6 - Transposta

def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

matriz_transposta = criar_matriz(10,10)
transposta(matriz_transposta)
printar_matriz(matriz_transposta)


#Exercício 8 - Xadrez

def xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i%2 == j%2:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return

matriz_xadrez = criar_matriz(8,8)
xadrez(matriz_xadrez)
printar_matriz(matriz_xadrez)
plotar_matriz(matriz_xadrez)

#Exercício 9 - Circulo

def circulo(matriz):
    raio = len(matriz)/2
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i - raio) ** 2 + (j - raio) ** 2 <= raio ** 2:
                matriz[i][j] = i
            else:
                matriz[i][j] = 0
    return

matriz_circulo = criar_matriz(1000,1000)
circulo(matriz_circulo)
plotar_matriz(matriz_circulo)









