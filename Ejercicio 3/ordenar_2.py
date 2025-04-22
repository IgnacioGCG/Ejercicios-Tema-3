from lanzador import naves
class nave_mas_pequena_y_grande:
    # Mostrar información de la nave más pequeña y la más grande
    nave_mas_pequena = min(naves, key=lambda x: x["longitud"])
    nave_mas_grande = max(naves, key=lambda x: x["longitud"])
