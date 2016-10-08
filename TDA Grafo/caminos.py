from grafo import Digraph

INFINITE = 999999


class caminos:
    def __init__(self, grafo, origen):
        self.origen = origen
        self.INFINITE = 99999999
        self.grafo = grafo
        pass

    def distancia(self, v):
        pass

    def camino(self, v):
        pass

    def visitado(self, v):
        return self.distancia(v) < INFINITE

graph = Digraph(5)
graph.add_edge(3, 2, 5)
graph.add_edge(1, 3, 5)
