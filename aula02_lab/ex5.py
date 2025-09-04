import numpy as np

def insereVertice(matriz):

    lin = len(matriz)
    col = len(matriz[0])
    
    
    for i in range (lin):
        matriz[i].append(0)
    
    matriz.append([0] * (len(matriz) + 1))
    
    matriz = np.array(matriz)
    print (matriz)
        
insereVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
