def analiseBFS(G, v, analisado):
    Q = []
    Q.append(v)

    while(len(Q) > 0):  
        v = Q.pop(0)
        if v not in analisado:
            analisado.append(v)
            for adj_v in G[v]:
                if adj_v not in analisado and adj_v not in Q:
                    Q.append(adj_v)

    return analisado

def BFS(G, v):
    analisado = []
    for key in G:
        if key not in analisado:
            analisado = analiseBFS(G, key, analisado)

    return analisado

def analiseDFS(G, v, analisado):
    analisado.append(v)
    for i in G[v]:
        if i not in analisado:
            analiseDFS(G, i, analisado)

    return analisado

def DFS(G, v):
    analisado = []
    
    analiseDFS(G, v, analisado)

    return analisado
