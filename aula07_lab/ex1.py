def ordenacaoTopologica(listaAdj):
    
    resultado = []
    visitado = []
    x = listaAdj[0]
    
    def tempoRecurs(x):
                
        visitado.append(x)

        for i in listaAdj[x]:   
           if i not in visitado:
                tempoRecurs(i)   
        
        resultado.insert(0, x)            
    
    
    tempoRecurs(x[0])
    for x in listaAdj:
        if x not in visitado:
            tempoRecurs(x)

    print (resultado)

ordenacaoTopologica({0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]})
