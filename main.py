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

import sys
from igraph import *
from Inicializacao import (dataSet as ds)
from Metodos import (caracteristicas as car)
from Inicializacao import (grafo as gr)
from Metodos import (buscas as bc)

'''Core do programa'''


def main(instancia):
    # chama a função para ler arquivo e retorna a matriz numpy
    matriz = ds.leArquivo(instancia)

    # chama a função que retorna as dimensões da matriz
    dimensoes = car.dimensoesMatriz(matriz)

    # chama a função que salva e imprime os resultados obtidos
    ds.salvaInfos(instancia, dimensoes)

    dic = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4], 6:[]}
    
    teste = bc.DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)

"""Chamada a função main()
   Argumento Entrada: [1] dataset"""


if __name__ == '__main__':
    main(str(sys.argv[1]))
