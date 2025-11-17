def criaListaAdjacencias(matriz):
    dicio = {}
    for i in range(len(matriz)):
        dicio[i] = []
        for j in range(len(matriz)):
            if(matriz[i][j] != 0):
                for _ in range(matriz[i][j]):
                    dicio[i].append(j)
    return dicio

def caminhoEuleriano(grafo):
    vertices = len(grafo)
    vertices_impares = 0
    i = 0

    listaAdj = criaListaAdjacencias(grafo)
    #aplicar dfs para verificar se é conexo

    visitado = []
    pilha = [0]
    while pilha:
        var = pilha.pop()

        for adjacente in reversed(listaAdj[var]):
            if adjacente not in visitado and adjacente not in pilha:
                pilha.append(adjacente)

        if var not in visitado:
            visitado.append(var)

        # DFS completa
        # if not pilha:
        #     for i in listaAdj.keys():
        #         if i not in visitado:
        #             pilha.append(i)
        
    if len(visitado) != vertices:
        return print(False)

    while vertices_impares <= 2 and i < vertices:

        grau = 0
        for j in grafo[i]:
            grau += j

        # So funciona quando o vertice estiver isolado
        # e nao funciona para componentes conexos
        if grau == 0:
            return print('False')
        
        if grau % 2 != 0:
            vertices_impares += 1
        
        i += 1
        
    if vertices_impares > 2 or vertices_impares == 1:
        return print('False')
    else:
        return print('True')
    
caminhoEuleriano([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]])