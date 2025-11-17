def criaListaAdjacencias(matriz):
    dicio = {}
    for i in range(len(matriz)):
        dicio[i] = []
        for j in range(len(matriz)):
            if(matriz[i][j] != 0):
                for _ in range(matriz[i][j]):
                    dicio[i].append(j)
    return dicio

def dijkstra(matriz, vinicio, vfim):
    
    listaAdj = criaListaAdjacencias(matriz)

    
    custo = []
    rota = []
    
    for i in range (len(matriz)):
        N = listaAdj[i].keys()
        custo[i] = -1
        rota[i] = vinicio
        
    custo[vinicio] = 0
    A = listaAdj.keys()
    F = []
    
    while A != 0:
        v = min(A)
        F.append(v)
        A.remove(v)
        N.remove(v)
           

    