def criaDicionario(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    
    dicionario = {}
    
    for i in range(lin):
        for j in range(col):
            
            if matriz[i][j] != 0:
                if i not in dicionario:
                    dicionario[i] = []
                    
                # Adiciona o índice da coluna à lista correspondente
                for _ in range(matriz[i][j]):
                    dicionario[i].append(j)
                    
    print(dicionario)