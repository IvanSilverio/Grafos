import numpy as np

def removeAresta(matriz, vi, vj):
    
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0
   
    matriz = np.array(matriz)
    print (matriz)
    
    
removeAresta([[0, 1,0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 1, 0)