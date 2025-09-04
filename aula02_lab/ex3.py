def calcDensidade(matriz):
    
    lin = len(matriz)
    col = len(matriz[0])
    
    E = 0
    
    for vi in range(lin):
        for vj in range(col):
           if matriz[vi][vj] == 1:
               E+=1
    d = float(E / (lin * (lin - 1)))
    print (f"{d:.3f}")
            
    
                
                
    
    