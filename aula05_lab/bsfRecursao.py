def BFS(listaAdj, v):
    
    analisado = []
    
    def recursao (listaAdj, v):
    
        q = []
        q.append(v)
        
        while  q != []:
            #v recebe o primeiro vertice da fila de q
            v = q.pop(0)
            if v not in analisado:
                for i in listaAdj[v]:
                    
                    #se os adj nao estiverem em q (visitado) e em analisado, apenda em q
                    if i not in q and i not in analisado:
                        q.append(i)
                            
                    #apenda v em analisado
                analisado.append(v)
        
    
    recursao (listaAdj, v)
    # while len(listaAdj) > len(analisado): #se as listas forem diferentes, analisa na lista adj os que nao estao em analisado
    for num in listaAdj:
        if num not in analisado:
        
            recursao(listaAdj, num)
        
    print(analisado)
        

BFS({0: [0, 2, 4], 1: [2, 4], 2: [0, 1, 2, 4], 3: [8], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5], 7: [], 8: [3]}, 0)
