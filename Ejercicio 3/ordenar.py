from lanzador import naves
class naves_ordenadas:
    # Ordenar la lista de naves por nombre ascendente y longitud descendente
    naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))
