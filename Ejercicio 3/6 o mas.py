from lanzador import naves
class naves_seis_pasajeros:
    # Mostrar todas las naves que pueden llevar seis o más pasajeros
    naves_seis_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]
# Listar todas las naves que pueden llevar seis o más pasajeros
naves_seis_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]
