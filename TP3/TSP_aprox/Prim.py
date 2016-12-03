from Arista import Arista
class Prim:
    def calcular_tendido_minimo(self, grafo, inicial):
        tendido_minimo = set()
        total = 0
        auxiliar = set()
        auxiliar.add(inicial)
        vertices = len(grafo)
        while len(auxiliar) != vertices:
            cruza = set()
            for primer_iterador in auxiliar:
                for segundo_iterador in range(vertices):
                    if segundo_iterador not in auxiliar and grafo[primer_iterador][segundo_iterador] != 0:
                        cruza.add((primer_iterador, segundo_iterador))
            if len(cruza) > 0:
                arista = sorted(cruza, key=lambda e: grafo[e[0]][e[1]])[0]
                tendido_minimo.add(arista)
                total = total + grafo[arista[0]][arista[1]]
                auxiliar.add(arista[1])
        return tendido_minimo

    # def duplicar_camino(mst):
    #     return_mst = set(mst)
    #     for arista in mst:
    #         nueva_arista =
    #         return_mst.add(nueva_arista)
    #     return return_mst