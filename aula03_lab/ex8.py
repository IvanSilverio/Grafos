def verificaAdjacenciaLista(listaAdj, vi, vj):
    
    if vj in listaAdj[vi] and vi in listaAdj[vj]:
        print ('True')
        
    else:
        print ('False')

verificaAdjacenciaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 3)
