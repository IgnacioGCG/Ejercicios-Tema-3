from lanzador import naves
class naves_mas_pasajeros:
    def __init__(self, naves):
        self.naves = naves

    def obtener_naves_mas_pasajeros(self):
        # Filtrar las naves que tienen 6 o más pasajeros
        naves_filtradas = [nave for nave in self.naves if nave["pasajeros"] >= 6]
        
        # Ordenar las naves filtradas por la cantidad de pasajeros
        naves_ordenadas = sorted(naves_filtradas, key=lambda x: x["pasajeros"], reverse=True)
        
        # Retornar las cinco naves con mayor cantidad de pasajeros
        return naves_ordenadas[:5]
# Determinar las cinco naves con mayor cantidad de pasajeros
naves_mas_pasajeros = sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5]