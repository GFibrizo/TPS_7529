from grafo import Digraph
from CaminoMinimo import CaminoMinimo
import heapq

class Dijkstra(CaminoMinimo):

    def __init__(self, grafo, origen, destino):
        CaminoMinimo.__init__(self, grafo, origen, destino)
        self.dist_heap = []
        #heapq.heapify(self.dist_heap)
        for i in xrange(self.grafo.V()):
            self.distancias.append(self.INFINITE)
            heapq.heappush(self.dist_heap, [self.distancia(i), i])
        self.distancia_actual = 0
        self._camino_minimo()

    def _camino_minimo(self):
        vertice = self.origen
        self.distancias[vertice] = self.distancia_actual
        self.padre[vertice] = None
        anterior = None
        while (len(self.visitados) < self.grafo.V()):
            for vecino in self.grafo.adj(vertice):
                nueva_dist = self.distancia_actual + self.grafo.obtener_arista(vertice, vecino).weight()
                if (not self.visitado(vecino)) or (nueva_dist < self.distancias[vecino]):
                    self.distancias[vecino] = nueva_dist
                    self.padre[vecino] = vertice
            self.visitados.add(vertice)
            self.distancia_actual, vertice = self._obtener_siguiente()

    def _obtener_siguiente(self):
        heap = []
        heapq.heapify(heap)
        for i in xrange(self.grafo.V()):
            if (i not in self.visitados):
                heapq.heappush(heap, [self.distancia(i), i])
        if len(heap) == 0:
            return self.distancia_actual, None
        return heapq.heappop(heap)





graph = Digraph(8)
graph.add_edge(0, 1, 1)     # 1 --
graph.add_edge(0, 2, 3)     # 3
graph.add_edge(2, 3, 1)     # 1
graph.add_edge(3, 4, 1)     # 1
graph.add_edge(1, 4, 1)     # 4
graph.add_edge(1, 2, 1)     # 1
graph.add_edge(4, 5, 5)     # 2
graph.add_edge(5, 6, 1)     # 1
graph.add_edge(5, 7, 4)     # 4
graph.add_edge(6, 7, 1)     # 1
search = Dijkstra(graph, 0, 7)
print search.camino(7)
print search.distancia(7)