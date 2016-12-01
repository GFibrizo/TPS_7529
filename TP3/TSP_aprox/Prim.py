class Prim:
    def calcular_tendido_minimo(self, grafo):
        tendido_minimo = set();
        auxiliar = set();
        auxiliar.add(0);
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
                auxiliar.add(arista[1])
        return tendido_minimo