from grafo import Digraph
from CaminoMinimo import CaminoMinimo
from math import sqrt
import heapq

class A_estrella(CaminoMinimo):

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
                    self.distancias[vecino] = nueva_dist + heuristic(vertice, vecino)
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



def heuristic(curr, dst):
    diff1 = locations[dst][0] - locations[curr][0]
    diff2 = locations[dst][1] - locations[curr][1]
    return sqrt((diff1**2) + (diff2**2))




graph = Digraph(9)
locations = [(0,0), (0,1), (0,2), (1,2), (1,0), (2,0), (2,1), (1,1), (2,2)]
graph.add_edge(0, 1, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 3, 1)
graph.add_edge(0, 4, 5)
graph.add_edge(4, 5, 5)
graph.add_edge(5, 6, 5)
graph.add_edge(0, 7, 10)
graph.add_edge(6, 8, 4)
graph.add_edge(3, 8, 1)
graph.add_edge(7, 8, 2)
search = A_estrella(graph, 0, 8)
print search.distancia(8)
print search.camino(8)