def dimensaoMatriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    val_diagonal = []
    for i in range(lin):
        val_diagonal.append(matriz[i][i])

    # Converte cada número em string e junta-os com um espaço
    diagonal_string = ' '.join(str(x) for x in val_diagonal)

    print(f"({lin}, {col}) [{diagonal_string}]")
    return