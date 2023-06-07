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
    analisado = analiseBFS(G, v, analisado)
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


def DFSiterativo(G, v):
    analisado = []
    pilha = [v]
    controle = 0

    while(pilha):
        if pilha[len(pilha) - 1] not in analisado:
            analisado.append(pilha[len(pilha) - 1])
            
        for i in G[pilha[len(pilha) - 1]]:
            if i not in pilha and i not in analisado:
                pilha.append(i)
                controle = 0
                break
            else:
                controle = 1

        if controle == 1:
            pilha.pop()

    for n in list(G.keys()):
        if n not in analisado:
            analisado.append(n)
            
    return analisado

def tempoDFS(listaAdj, v, analisado, tempo, listaTempo):

    listaTempo[v] = "{}/".format(tempo)
    tempo += 1

    analisado.append(v)
    for i in listaAdj[v]:
        if i not in analisado:
            tempo = tempoDFS(listaAdj, i, analisado, tempo, listaTempo)

    listaTempo[v] += "{}".format(tempo)
    tempo += 1
    

    return tempo

def temposVertices(listaAdj, v):
    listaTempo = {}
    analisado = []
    tempo = 1
    for i in listaAdj:
        listaTempo[i] = ""
    
    listaTempo[v] = "{}/".format(tempo)
    tempo += 1

    analisado.append(v)
    for i in listaAdj[v]:
        if i not in analisado:
            tempo = tempoDFS(listaAdj, i, analisado, tempo, listaTempo)

    listaTempo[v] += "{}".format(tempo)
    tempo += 1

    for key in listaAdj:
        if key not in analisado:
            tempo = tempoDFS(listaAdj, key, analisado, tempo, listaTempo)

    return listaTempo

def classificaArestaDFS(listaAdj):
    cor = {}
    tipoAresta = {}
    tempoD = {}
    tempoT = {}
    tempo = 0

    for v in listaAdj.keys():
        cor[v] = "branco"
        tempoD[v] = ""
        tempoT[v] = ""

    def visitaDFS(v, tempo):
        cor[v] = "cinza"
        tempo += 1
        tempoD[v] = tempo

        for vertice in listaAdj[v]:
            if cor[vertice] == "branco":
                tipoAresta[(v, vertice)] = "Tree"
                tempo = visitaDFS(vertice)

            elif cor[vertice] == 'cinza':
                tipoAresta[(v, vertice)] = "Back"

            else:
                if tempoD[v] < tempoD[vertice]:
                    tipoAresta[(v, vertice)] = "Forward"

                else:
                    tipoAresta[(v, vertice)] = "Cross"

        cor[v] = "preto"
        tempo += 1
        tempoT[v] = tempo

        return tempo

    for v in listaAdj.keys():
        if cor[v] == "branco":
            tempo = visitaDFS(v)

    msg = ""
    for (v, vertice) in tipoAresta.keys():
        msg += str(v) + " " + str(vertice) + " " + tipoAresta[(v, vertice)] + "\n"

    return msg

def ordenacaoTopologica(listaAdj):
    L = {}
    cor = {}
    tipoAresta = {}
    tempoD = {}
    tempoT = {}
    tempo = 0

    for v in listaAdj.keys():
        cor[v] = "branco"
        tempoD[v] = ""
        tempoT[v] = ""

    for v in listaAdj.keys():
        if cor[v] == "branco":
            tempo = visitaDFS(v, tempo)

    def visitaDFS(v, tempo):
        cor[v] = "cinza"
        tempo += 1
        tempoD[v] = tempo

        for vertice in listaAdj[v]:
            if cor[vertice] == "branco":
                tipoAresta[(v, vertice)] = "Tree"
                tempo = visitaDFS(vertice)

            elif cor[vertice] == 'cinza':
                tipoAresta[(v, vertice)] = "Back"

            else:
                if tempoD[v] < tempoD[vertice]:
                    tipoAresta[(v, vertice)] = "Forward"
                    
                else:
                    tipoAresta[(v, vertice)] = "Cross"

        cor[v] = "preto"
        tempo += 1
        tempoT[v] = tempo

        return tempo

    return [k for k, _ in sorted(L.items(), key=lambda item: item[1], reverse=True)]