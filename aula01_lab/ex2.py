def valorCelula(matriz, i, j):
    
    lin = len(matriz)
    col = len(matriz[0])
    
    if i >= lin or j >= col:
        print ('Erro')
        
    else: print (f"Celula[{i}][{j}] = {matriz[i][j]}")
    