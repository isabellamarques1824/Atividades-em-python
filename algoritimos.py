def acha_menor(lista):
    ind = 0
    for i in range(len(lista)):
        if lista[i] < lista[ind]:
            ind = i
    return ind


def selection_sort(lista):
    lista_nova = []
    while lista:
        menor = acha_menor(lista)
        lista_nova.append(lista[menor])
        lista.pop(menor)
    return lista_nova


def selection_sort_menos_ruim(lista):
    for i in range(len(lista)):
        menor = acha_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
        print(lista)


lista = [3, 1, 5, 6, 2, 4, 7]


# isso é uma tentativa n to conseguindo fazer

def acha_raiz(n):
    ini = 0
    while True:
        chute = (ini + n) / 2
        if chute ** 2 > n:
            n = chute
        elif chute ** 2 < n:
            ini = chute
        print(chute)


def bubble_sort(lista):
    for i in range(len(lista)):
        trocas = 0
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocas += 1
        if trocas == 0:
            break
    return
