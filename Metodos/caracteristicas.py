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


def infosMatriz(matriz):
    # shape() é uma função da biblioteca numpy que retorna as dimensões do array
    dimensao = np.shape(matriz)

    return dimensao
