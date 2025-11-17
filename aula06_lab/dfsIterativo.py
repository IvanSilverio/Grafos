def DFS (grafo, v):
    
     # Inicialização conforme o pseudocódigo:
    # idsVertices (conjunto de todos os vértices não visitados)
    idsVertices = set(grafo.keys()) 
    sequencia = [] # sequencia (vértices visitados)
    P = [v] # P (pilha da DFS)

    while idsVertices: # Loop 5: Enquanto houver vértices para visitar
        while P: # Loop 6: Enquanto a pilha não estiver vazia (DFS em um componente)
            
            t = P[-1] # Linha 7: Pega o topo da pilha
            
            if t not in sequencia: # Linha 8-9: Se não foi visitado, visita
                sequencia.append(t)
            
            # Linha 10: Calcula os vizinhos viáveis (não visitados)
            # REQUER CORREÇÃO: 'adj_Viaveis' deve ser calculado para 't'
            # (grafo[t] é a listaAdj[t])
            adj_Viaveis = [vizinho for vizinho in grafo.get(t, []) if vizinho not in sequencia]
            
            if adj_Viaveis: # Linha 11-12: Se houver vizinhos viáveis, avança
                P.append(adj_Viaveis[0]) # Adiciona o primeiro vizinho à pilha
            else: # Linha 13-14: Senão, recua (backtrack)
                P.pop() # Remove 't' da pilha
        
        # FIM DO while P (Fim do componente conexo)

        # Linha 15: Atualiza idsVertices para os não visitados
        idsVertices.difference_update(sequencia)

        # Linha 16-17: Se ainda há vértices não visitados (outro componente)
        if idsVertices:
            # Pega o primeiro vértice do conjunto de não visitados
            proximo_v = next(iter(idsVertices))
            P.append(proximo_v) # Inicia nova DFS a partir dele
            
    print (sequencia)
    




DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
