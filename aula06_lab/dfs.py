def DFS (grafo, v):
    visitado = []
    
    def recursao (v):
        visitado[0].append(v)
        
        for adj in grafo[v]:
            if adj not in visitado:
                recursao (adj)
      
    recursao(v) 
    if len(grafo) != len(visitado):  
        for valor in grafo: 
            if valor not in visitado:
                recursao (v)
    
    print (visitado)

DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
