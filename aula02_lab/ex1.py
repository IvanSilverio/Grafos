def tipoGrafo(matriz):

    lin = len(matriz)
    col = len(matriz[0])
    resp = '0'
    simples = True
    
    for i in range (lin):
        for j in range (col):
            
            if matriz[i][j] != matriz[j][i]:
                resp = '1'
                simples = False
                break
            
        if simples == False:
            break
                
        
    if resp == '0':
        for i in range (lin): 
            
            if matriz[i][i] != 0:
                resp = '30'
                break
        print (resp)
        return
    
    if resp == '0':
        mult = False
        for i in range (lin):
            for j in range (col):
                if matriz[i][j] > 1:
                    resp = '21'
                    mult = True
                    break
            
            if mult == True:
                print (resp)
                return
            
    if resp == '0':
        print (resp)
        return
            
    if resp == '1':
        for i in range (lin): 
            
            if matriz[i][i] != 0:
                resp = '31'
                print (resp)
                return
    
    
    for i in range (lin):
        for j in range (col):
            if matriz[i][j] > 1:  
                resp = '21'
                print (resp)  
                return
            
    print (resp)
    
            
tipoGrafo([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
                
           

#CÓDIGO DO GEMINI, MAIS EFICIENTE

# def tipoGrafo(matriz):
#     is_digraph = False
#     has_loops = False
#     has_multiple_edges = False
#     n = len(matriz)

#     # Verifica se a matriz é quadrada
#     if n == 0 or any(len(row) != n for row in matriz):
#         return "Entrada inválida: a matriz deve ser quadrada."

#     # Itera sobre a matriz para detectar as características do grafo
#     for i in range(n):
#         for j in range(n):
#             # Verifica se é um dígrafo (grafo dirigido)
#             if matriz[i][j] != matriz[j][i]:
#                 is_digraph = True
            
#             # Verifica arestas múltiplas
#             if matriz[i][j] > 1:
#                 has_multiple_edges = True

#         # Verifica laços (loops) na diagonal principal
#         if matriz[i][i] != 0:
#             has_loops = True

#     # Classifica o grafo com base nas características encontradas
#     if has_loops:
#         if is_digraph:
#             return 31  # Pseudografo dirigido
#         else:
#             return 30  # Pseudografo
#     elif has_multiple_edges:
#         if is_digraph:
#             return 21  # Multigrafo dirigido
#         else:
#             return 20  # Multigrafo
#     elif is_digraph:
#         return 1   # Dígrafo
#     else:
#         return 0   # Grafo simples

# # --- Exemplos de uso ---

# # Grafo simples
# matriz_simples = [[0, 1, 0, 0], 
#                   [1, 0, 1, 1], 
#                   [0, 1, 0, 1], 
#                   [0, 1, 1, 0]]
# print(f"Tipo da matriz simples: {tipoGrafo(matriz_simples)}")  # Saída: 0

# # Dígrafo
# matriz_digrafo = [[0, 1, 0], 
#                   [0, 0, 1], 
#                   [1, 0, 0]]
# print(f"Tipo da matriz de dígrafo: {tipoGrafo(matriz_digrafo)}")  # Saída: 1

# # Multigrafo
# matriz_multigrafo = [[0, 2, 0], 
#                      [2, 0, 1], 
#                      [0, 1, 0]]
# print(f"Tipo da matriz de multigrafo: {tipoGrafo(matriz_multigrafo)}")  # Saída: 20

# # Multigrafo dirigido
# matriz_multigrafo_dirigido = [[0, 2, 0], 
#                               [1, 0, 1], 
#                               [0, 0, 0]]
# print(f"Tipo da matriz de multigrafo dirigido: {tipoGrafo(matriz_multigrafo_dirigido)}")  # Saída: 21

# # Pseudografo
# matriz_pseudografo = [[0, 1, 0], 
#                       [1, 1, 1], 
#                       [0, 1, 0]]
# print(f"Tipo da matriz de pseudografo: {tipoGrafo(matriz_pseudografo)}")  # Saída: 30

# # Pseudografo dirigido
# matriz_pseudografo_dirigido = [[0, 1, 0], 
#                                [0, 1, 1], 
#                                [0, 0, 0]]
# print(f"Tipo da matriz de pseudografo dirigido: {tipoGrafo(matriz_pseudografo_dirigido)}")  # Saída: 31