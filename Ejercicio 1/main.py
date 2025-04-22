def hanoi(n, origen='A', destino='C', auxiliar='B', mostrar=False):
    movimientos = []

    def mover(n, origen, destino, auxiliar):
        if n == 1:
            if mostrar:
                print(f"Mover piedra 1 de {origen} a {destino}")
            movimientos.append((1, origen, destino))
        else:
            mover(n - 1, origen, auxiliar, destino)
            if mostrar:
                print(f"Mover piedra {n} de {origen} a {destino}")
            movimientos.append((n, origen, destino))
            mover(n - 1, auxiliar, destino, origen)

    mover(n, origen, destino, auxiliar)
    return movimientos

# === USO PRINCIPAL ===
if __name__ == "__main__":
    piedras = 74
    total = 2 ** piedras - 1
    print(f"Total de movimientos necesarios para {piedras} piedras: {total}")
    
    # Para probar visualmente, puedes hacer esto con menos piedras:
    # hanoi(3, mostrar=True)
# Basicamente, para explicar el algoritmo que resuelve el problema de las Torres de Hanoi:
# 1. Mueve n-1 piedras de la torre A a la torre B, usando la torre C como auxiliar.