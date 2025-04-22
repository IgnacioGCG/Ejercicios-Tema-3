def determinante_iterativo_3x3(m):
    return (
        m[0][0]*m[1][1]*m[2][2] +
        m[0][1]*m[1][2]*m[2][0] +
        m[0][2]*m[1][0]*m[2][1] -
        m[0][2]*m[1][1]*m[2][0] -
        m[0][0]*m[1][2]*m[2][1] -
        m[0][1]*m[1][0]*m[2][2]
    )

# Definimos una matriz 3x3 de ejemplo
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mismo ejemplo
print("Determinante (método iterativo):", determinante_iterativo_3x3(matriz_3x3))
