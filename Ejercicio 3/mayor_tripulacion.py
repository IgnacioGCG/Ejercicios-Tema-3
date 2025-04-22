from lanzador import naves
class nave_mas_tripulantes:
    # Mostrar información de la nave que requiere la mayor cantidad de tripulación
    nave_mas_tripulantes = max(naves, key=lambda x: x["tripulantes"])
# Determinar la nave que requiere la mayor cantidad de tripulación
nave_mas_tripulantes = max(naves, key=lambda x: x["tripulantes"])