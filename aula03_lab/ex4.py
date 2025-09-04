def insereAresta(listaAdj, vi, vj):
    
    grafo_simples = True
    
    for i in listaAdj:
        if grafo_simples == False:
            break
        
        for j in listaAdj[i]:
                        
            if i not in listaAdj[j]:
                grafo_simples = False
                break
    
    if grafo_simples == True:
        
        listaAdj[vi].extend({vj})
        listaAdj[vj].extend({vi})
        
        listaAdj[vi].sort()
        listaAdj[vj].sort()
        
    else:
        listaAdj[vi].extend({vj})
        listaAdj[vi].sort()
    
    print (listaAdj)

insereAresta({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)
