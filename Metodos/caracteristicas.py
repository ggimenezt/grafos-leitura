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


def tipoGrafoMatriz(matriz):
    tipo = '0'
    flag = 0
    tam = dimensoesMatriz(matriz)[0]

    if np.sum(np.diagonal(matriz)) > 0:
        tipo = '3'

    for x in range(tam):
        for y in range(tam):
            if tipo != '3':
                if matriz[x][y] > 1:
                    tipo = '2'

            if x != y:
                if matriz[x][y] != matriz[y][x]:
                    flag = 1

    if flag == 1:
        tipo += '1'

    else:
        tipo += '0'

    return (int(tipo))

def tipoGrafoLista(listaAdj):
    tipo = '0'
    flag = '0'

    for i in listaAdj:
        if i in listaAdj[i]:
            tipo = '3'
    
    if tipo != '3':
        for i in listaAdj:
            for j in range(len(listaAdj[i])-1):
                if listaAdj[i][j] == listaAdj[i][j+1]:
                    tipo  = '2'
    
    for i in listaAdj:
        for j in range(len(listaAdj[i])):
            if i not in listaAdj[listaAdj[i][j]]:
                flag = '1'

    return (int(tipo+flag))


def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:
        adjacencia = True
    else:
        adjacencia = False

    return adjacencia

def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi]:
        return True
    else:
        return False


def calcDensidade(matriz):
    densidade = 0
    arestas = np.sum(matriz)
    nos = np.shape(matriz)[0]

    densidade = round(arestas/(nos*(nos-1)), 3)

    return densidade

def calcDensidadeLista(listaAdj):
    arestas = 0
    vertices = len(listaAdj)

    for i in listaAdj:
        arestas += len(listaAdj[i])

    densidade = round(arestas/(vertices*(vertices-1)), 3)

    return densidade

def warshall(matriz):
    n = np.shape(matriz)[0]
    R = matriz

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][j] == 1 or (R[i][k] == 1 and R[k][j] == 1):
                    R[i][j] = 1
                else:
                    R[i][j] = R[i][j]

    return np.array(R)

def caminhoEuleriano(matriz):
    n = np.shape(matriz)[0]
    total = 0
    i = 0

    while total <= 2 and i < n:
        print(i)
        grau = np.sum(matriz[i])

        if grau%2 !=0:
            total += 1

        i+=1

    if total > 2:
        return False
    
    else:
        return True
    
def verifica_dag(listaAdj):
    arestas = []
    fontes = []

    for vertice in listaAdj:
        if not any(vertice in adjacentes for adjacentes in listaAdj.values()):
            fontes.append(vertice)

    for vertice in listaAdj:
        for adjacente in listaAdj[vertice]:
            arestas.append((vertice, adjacente))

    while fontes:
        vertice = fontes[0]
        del fontes[0]

        for aresta in list(arestas):
            if aresta[0] == vertice:
                adjacente = aresta[1]
                arestas.remove(aresta)
                if not any(adjacente == adj[1] for adj in arestas):
                    fontes.append(adjacente)

    if arestas:
        print("NÃO DAG")
    else:
        print("DAG")

    