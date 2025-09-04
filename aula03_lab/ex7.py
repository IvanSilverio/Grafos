def removeVerticeLista(listaAdj, vi):
    
    listaAdj.pop(vi)

    for i in listaAdj:
        
        if vi in listaAdj[i]:
            while vi in listaAdj[i]:
                listaAdj[i].remove(vi)
    
    print(listaAdj)
            

    
removeVerticeLista({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 2)
