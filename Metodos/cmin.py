import numpy as np

def bellmanFord(G, vOrigem, vDestino):
    G = np.array(G)
    custo = []
    rota = []
    V = np.shape(G)[0]

    custo = [float('inf')] * V
    rota = [0] * V

    custo[0] = 0
    for i in range(V):
        for v in range(V):
            for u in range(V):
                if G[v, u] != -1:
                    if custo[u] > custo[v] + G[v, u]:
                        custo[u] = custo[v] + G[v, u]
                        rota[u] = v
    
    for v in range(V):
        for u in range(V):
            if G[v, u] != -1:
                if custo[u] > custo[v] + G[v, u]:
                    return False
                
    caminho = [vDestino]
    custoCam = custo[vDestino]

    while vDestino != vOrigem:
        vDestino = rota[vDestino]
        caminho.insert(0, vDestino)

    return (caminho, custoCam)


def dijkstra(G, vOrigem, vDestino):
    caminho = []
    V = np.shape(G)[0]
    custo = [float('inf')] * V
    rota = [0] * V

    custo[0] = 0
    rota[0] = 0

    A = set(range(V))
    F = set()

    while A:
        v = min(A, key=lambda x: custo[x])
        F.add(v)
        A.remove(v)

        for u in range(V):
            if u not in F:
                if G[v][u] != -1:
                    if custo[v] + G[v][u] < custo[u]:
                        custo[u] = custo[v] + G[v][u]
                        rota[u] = v
    
    j = vDestino
    while vDestino != vOrigem:
        caminho.append(vDestino)
        vDestino = rota[vDestino]
    caminho.append(vOrigem)
    caminho.reverse()

    custoMin = int(custo[j])

    return (caminho, custoMin)

def floydWarshall(G):
    n = np.shape(G)[0]
    D = np.copy(G)

    D[D == -1] = 99999

    for k in range(0, n):
        for v in range(0, n):
            for u in range(0, n):
                if D[v][u] > D[v][k] + D[k][u]:
                    D[v][u] = D[v][k] + D[k][u]

    D[D == 99999] = -1

    saida = [list(row) for row in D]

    return saida