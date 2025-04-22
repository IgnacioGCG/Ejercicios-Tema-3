from lanzador import naves
class info_cometa_veloz_titan_cosmos:
    # Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
    info_cometa_veloz = next((nave for nave in naves if nave["nombre"] == "Cometa Veloz"), None)
    info_titan_cosmos = next((nave for nave in naves if nave["nombre"] == "Titán del Cosmos"), None)
