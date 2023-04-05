"""=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Gustavo Gimenez Teixeira - 2021006467

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

30/03/2023
===================================================="""

import numpy as np

"""
função para ler as dimensoes da matriz utilizando a função shape da biblioteca numpy
"""


def dimensoesMatriz(matriz):
    # shape() é uma função da biblioteca numpy que retorna as dimensões do array
    dimensao = np.shape(matriz)

    return dimensao


def tipoGrafo(matriz):
    tipo = '0'
    flag = 0
    tam = dimensoesMatriz(matriz)[0]

    if np.sum(np.diagonal(matriz)) > 0:
        tipo = '3'

    else:
        for x in range(tam):
            for y in range(tam):
                if matriz[x][y] > 1:
                    tipo = '2'

    for x in range(tam):
        for y in range(tam):
            if x != y:
                if matriz[x][y] != matriz[y][x]:
                    flag = 1

    if flag == 1:
        tipo += '1'

    else:
        tipo += '0'

    return (int(tipo))


def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:
        adjacencia = True
    else:
        adjacencia = False

    print(adjacencia)

    return adjacencia

# def calcDensidade(matriz):
