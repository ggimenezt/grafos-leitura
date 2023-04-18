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

def insereArestaLista(listaAdj, vi, vj):

    listaAdj[vi].append(vj)
    listaAdj[vj].append(vi)

    listaAdj[vi].sort()
    listaAdj[vj].sort()

    return listaAdj


def insereVertice(matriz):
    zerosLinhas = np.zeros(car.dimensoesMatriz(matriz)[0], dtype=int)
    zerosColunas = np.zeros((car.dimensoesMatriz(matriz)[0]+1, 1), dtype=int)
    matriz = np.vstack([matriz, zerosLinhas], dtype=int)
    matriz = np.hstack([matriz, zerosColunas], dtype=int)

    return matriz

def insereVerticeLista(listaAdj):
    listaAdj[len(listaAdj+1)] = []

    return listaAdj


def removeAresta(matriz, vi, vj):
    tipo = car.tipoGrafo(matriz)

    if tipo == 0 or tipo == 20 or tipo == 30:
        matriz[vi][vj] -= 1
        matriz[vj][vi] -= 1

    else:
        matriz[vi][vj] -= 1

    return matriz

def removeArestaLista(listaAdj, vi, vj):
    flag = 0

    for i in listaAdj:
        for j in range(len(listaAdj[i])):
            if i not in listaAdj[listaAdj[i][j]]:
                flag = '1'
                break

    if flag == 0:    
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)

    else:
        listaAdj[vi].remove(vj)
    
    listaAdj[vi].sort()
    listaAdj[vj].sort()

    return listaAdj


def removeVertice(matriz, vi):
    for i in range(car.dimensoesMatriz(matriz)[0]):
        matriz[vi][i] = -1
        matriz[i][vi] = -1

    return np.array(matriz)

def removeVerticeLista(listaAdj, vi):
    del listaAdj[vi]

    for i in listaAdj:
        for j in range(listaAdj[i].count(vi)):
            listaAdj[i].remove(vi)

    return listaAdj
