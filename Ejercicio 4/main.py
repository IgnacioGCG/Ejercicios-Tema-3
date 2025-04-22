# Representación de un polinomio como un diccionario
# Ejemplo: 3x^2 + 2x + 1 se representa como {2: 3, 1: 2, 0: 1}

def restar_polinomios(p1, p2):
    """Resta dos polinomios."""
    resultado = p1.copy()
    for exponente, coeficiente in p2.items():
        resultado[exponente] = resultado.get(exponente, 0) - coeficiente
        if resultado[exponente] == 0:
            del resultado[exponente]
    return resultado

def dividir_polinomios(p1, p2):
    """Divide dos polinomios (división sintética)."""
    if not p2:
        raise ValueError("El divisor no puede ser un polinomio vacío.")
    resultado = {}
    dividendo = p1.copy()
    while dividendo and max(dividendo) >= max(p2):
        exponente_dif = max(dividendo) - max(p2)
        coeficiente_dif = dividendo[max(dividendo)] / p2[max(p2)]
        resultado[exponente_dif] = coeficiente_dif
        # Resta el término correspondiente
        for exponente, coeficiente in p2.items():
            exponente_actual = exponente + exponente_dif
            dividendo[exponente_actual] = dividendo.get(exponente_actual, 0) - coeficiente * coeficiente_dif
            if dividendo[exponente_actual] == 0:
                del dividendo[exponente_actual]
    return resultado, dividendo  # Retorna cociente y residuo

def eliminar_termino(polinomio, exponente):
    """Elimina un término de un polinomio dado su exponente."""
    if exponente in polinomio:
        del polinomio[exponente]
    return polinomio

def existe_termino(polinomio, exponente):
    """Determina si un término específico existe en un polinomio."""
    return exponente in polinomio

# Ejemplo de uso
if __name__ == "__main__":
    p1 = {2: 3, 1: 2, 0: 1}  # 3x^2 + 2x + 1
    p2 = {1: 1, 0: 1}        # x + 1

    print("Resta:", restar_polinomios(p1, p2))
    cociente, residuo = dividir_polinomios(p1, p2)
    print("División: Cociente:", cociente, "Residuo:", residuo)
    print("Eliminar término:", eliminar_termino(p1, 1))
    print("Existe término (x^2):", existe_termino(p1, 2))