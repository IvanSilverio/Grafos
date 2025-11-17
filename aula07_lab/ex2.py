def temposVertices(listaAdj, v):
    
    resultado = {}
    visitado = []
    TD = [0] * len(listaAdj)
    TT = [0] * len(listaAdj)
    tempo = 0
    
    def tempoRecurs(x):
        
        nonlocal tempo
        tempo += 1
        TD[x] = tempo
        
        visitado.append(x)

       
        for i in listaAdj[x]:   
           if i not in visitado:
                tempoRecurs(i)
                
        tempo += 1
        TT[x] = tempo         
               
    
    tempoRecurs(v)
    for x in listaAdj:
        if x not in visitado:
            tempoRecurs(x)
    
    for i in range (len(listaAdj)):
        resultado[i] = (f'{TD[i]}/{TT[i]}')


    print (resultado)

temposVertices({0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}, 0)
