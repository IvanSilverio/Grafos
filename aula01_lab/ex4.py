def contaRegressivaRecursao (numero):
    if numero <= 0:
        return
    
    print(numero)   
    numero -=1
    contaRegressivaRecursao(numero)     