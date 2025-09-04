def calcDensidade(listaAdj):
    
    grafo_simples = True
    V = len (listaAdj)
    E = 0

    for i in listaAdj:
        E = E+1
        for j in listaAdj[i]:
               
            E = E + 1         
            if i not in listaAdj[j]:
                grafo_simples = False
    
    E  = (E - V) / 2
    
    if grafo_simples == True:
        D = (2 * E) / (V * (V-1))
    
    else: 
        D = E / (V * (V-1))
    
    print (f'{D:.3f}')
        
    
              

calcDensidade({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]})
