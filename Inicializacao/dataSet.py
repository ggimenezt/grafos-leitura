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
Função para ler as informações do arquivo e armazane-las em uma matriz do tipo numpy
"""


def leArquivo(instancia):
    # a variável caminho serve para guardar o path do arquivo a ser lido
    caminho = 'Instancias/' + instancia + '.txt'
    # with open() realiza o tratamento do arquivo de forma mais limpa
    with open(caminho, "rb") as file:
        # genfromtxt() gera uma matriz baseado nas informações do txt
        matriz = np.genfromtxt(file, dtype="int64")
    return matriz


"""
Função para salvar as informações obtidas em um arquivo e imprimir os mesmos na tela
"""


def salvaInfos(instancia, dimensoes):
    # stringResultado é a variavel que armazena a string com o nome da instancia e seus resultados
    stringResultado = instancia + ' ' + \
        str(dimensoes[0]) + ' ' + str(dimensoes[1])

    # caminho armazena o path do txt no qual ficara armazenado o resultado
    caminho = 'Resultados/resultado.txt'

    # with open() realiza o tratamento do arquivo de forma mais limpa
    with open(caminho, "a") as file:
        file.write(stringResultado + '\n')

    # imprime os resultados salvos no terminal
    print(stringResultado)


def criaListaAdjacencias(matriz):

    tam = np.shape(matriz)[0]
    listaAdj = {}

    for i in range(tam):
        listaAdj[i] = []
        for j in range(tam):
            if matriz[i][j] != 0 and matriz[i][j] != -1:
                for x in range(matriz[i][j]):
                    listaAdj[i].append(j)

    return listaAdj