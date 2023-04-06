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

from Metodos import (caracteristicas as car)
import numpy as np


def insereAresta(matriz, vi, vj):
    tipo = car.tipoGrafo(matriz)

    if tipo == 0 or tipo == 20 or tipo == 30:
        matriz[vi][vj] += 1
        matriz[vj][vi] += 1

    else:
        matriz[vi][vj] += 1

    return matriz


def insereVertice(matriz):
    zerosLinhas = np.zeros(car.dimensoesMatriz(matriz)[0], dtype=int)
    zerosColunas = np.zeros((car.dimensoesMatriz(matriz)[0]+1, 1), dtype=int)
    matriz = np.vstack([matriz, zerosLinhas], dtype=int)
    matriz = np.hstack([matriz, zerosColunas], dtype=int)

    return matriz


def removeAresta(matriz, vi, vj):
    tipo = car.tipoGrafo(matriz)

    if tipo == 0 or tipo == 20 or tipo == 30:
        matriz[vi][vj] -= 1
        matriz[vj][vi] -= 1

    else:
        matriz[vi][vj] -= 1

    return matriz


def removeVertice(matriz, vi):
    for i in range(car.dimensoesMatriz(matriz)[0]):
        matriz[vi][i] = -1
        matriz[i][vi] = -1

    return np.array(matriz)
