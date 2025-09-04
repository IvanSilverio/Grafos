import numpy as np

def removeVertice(matriz, v):

    for i in range (len(matriz)):
        matriz[v][i] = -1    
        matriz[i][v] = -1
    
    matriz = np.array(matriz)
    print (matriz)
    

removeVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2)