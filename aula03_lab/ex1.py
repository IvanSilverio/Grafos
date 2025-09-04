def criaListaAdjacencias(matriz):
    lin = len(matriz)
    col = len (matriz[0])
    dict = {}
    
    for i in range (lin):
        dict[i] = []
        
        for j in range (col):
            
            if matriz[i][j] > 0:
                dict[i].extend([j] * matriz[i][j])
                
    print (dict)

criaListaAdjacencias([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])