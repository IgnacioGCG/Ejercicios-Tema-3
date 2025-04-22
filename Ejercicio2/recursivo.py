def determinante_recursivo(matriz):
    # Caso base: matriz 2x2
    if len(matriz) == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    det = 0
    for c in range(len(matriz)):
        submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
        signo = (-1) ** c
        det += signo * matriz[0][c] * determinante_recursivo(submatriz)
    return det

# Ejemplo
matriz_3x3 = [
    [2, 5, 3],
    [1, -2, -1],
    [3, 6, 2]
]

print("Determinante (método recursivo):", determinante_recursivo(matriz_3x3))
