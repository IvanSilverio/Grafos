import sys
import numpy as np  # Importa a biblioteca numpy

def prim(matriz):
        
    num_vertices = len(matriz) # Usamos .shape para numpy arrays
    
    S = [0]
    
    N = set(range(1, num_vertices))
    
    # T: Lista para armazenar as arestas (u, v) da MST
    T = []
    
    # Custo total da MST
    custo_total = 0
    
    while len(T) < num_vertices - 1:
        if not N:
            break
        
        menor_peso = float('inf')
        melhor_aresta = None 
        
        for u in S:
            for v in N:
                peso = matriz[u, v] # Acesso em numpy pode ser matriz[u, v]
                
                if peso > 0 and peso < menor_peso:
                    menor_peso = peso
                    melhor_aresta = (u, v)
        
        if melhor_aresta is None:
            # Caso de grafo desconectado
            break
            
        (u_escolhido, v_escolhido) = melhor_aresta
        
        T.append(melhor_aresta)
        custo_total += menor_peso
        
        S.add(v_escolhido)
        N.remove(v_escolhido)
        
    # Retorna a Lista de arestas e o Inteiro do custo
    return T, custo_total

# --- Fim da função ---

# Matriz de adjacências (agora como numpy.ndarray)
matriz_exemplo = np.array([
    [0, 4, 0, 0, 0, 0, 0, 8, 0], 
    [4, 0, 8, 0, 0, 0, 0, 11, 0], 
    [0, 8, 0, 7, 0, 4, 0, 0, 2], 
    [0, 0, 7, 0, 9, 14, 0, 0, 0], 
    [0, 0, 0, 9, 0, 10, 0, 0, 0], 
    [0, 0, 4, 14, 10, 0, 2, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 1, 6], 
    [8, 11, 0, 0, 0, 0, 1, 0, 7], 
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
])

# Chama a função
arestas_mst, custo = prim(matriz_exemplo)

# Imprime a saída no formato exato solicitado: "lista custo"
print(f"{arestas_mst} {custo}")