def  removeArestaLista(listaAdj, vi, vj):
    
    grafo_simples = True
    
    for i in listaAdj:
        if grafo_simples == False:
            break
        
        for j in listaAdj[i]:
                        
            if i not in listaAdj[j]:
                grafo_simples = False
                break
    
    if grafo_simples == True:
            listaAdj[vj].remove(vi)
            listaAdj[vi].remove(vj)
      
    else:
            listaAdj[vi].remove(vj)
            
    print (listaAdj)


removeArestaLista({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 0, 2)
