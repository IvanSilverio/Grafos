def caminhoEuleriano(matriz):
    
    soma_grau = 0
    quant_v = len(matriz)
    soma_impar = 0
    euler = False
    
    k = 0

    for i in range (quant_v):
        soma_grau = 0
                
        while soma_impar <= 2 and k < i:
        
            for j in range (quant_v):
                
                soma_grau = soma_grau + matriz[i][j]
            
            #verifica se eh conexo
            if soma_grau == 0:
                print ("False")
                return
            
            #verifica se o vertice eh grau impar
            if soma_grau % 2 != 0:
                soma_impar = soma_impar + 1
                
            k+=1
    
    if soma_impar  != 1 and soma_impar <=2:
        euler = True
        
    else:
        euler = False
        
    print (euler)
            
            
caminhoEuleriano([[0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]])
