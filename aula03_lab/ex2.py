def tipoGrafoLista(listaAdj):
    
    simples = True
    digrafo = False
    mult = False
    pseudo = False
        
    for i in listaAdj:
        valores = []
        for j in listaAdj[i]:
         
            if i not in listaAdj[j]:
                simples = False
            
            if j in valores:
                mult = True
            valores.append(j)
            
            if i == j:
                pseudo = True
        
    if simples == True:
        
        resp = '0'
        if pseudo == True:
            resp = '30'
        elif mult == True:
            resp = '20'
    
    else:
        resp = '1'
        if pseudo == True:
            resp = '31'
        elif mult == True:
            resp = '21'
    
    print (resp)
        

tipoGrafoLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]})
