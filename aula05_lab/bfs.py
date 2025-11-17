def BFS(listaAdj, v):
    visitado = [v]
    sequencia = []

    while visitado:
        var = visitado.pop(0)
        for adjacente in listaAdj[var]:
            if adjacente not in visitado and adjacente not in sequencia:
                visitado.append(adjacente)
        
        if var not in sequencia:
            sequencia.append(var)
        
        if not visitado:
            for i in listaAdj.keys():
                if i not in sequencia:
                    visitado.append(i)
                    break
        
    return print(sequencia)

BFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0)