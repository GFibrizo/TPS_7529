from grafo import Digraph
from CaminoMinimo import CaminoMinimo
from math import sqrt
import heapq


class bfs(CaminoMinimo) :
    def __init__(self, grafo, origen, destino):
        CaminoMinimo.__init__(self,grafo, origen, destino)
        self.aristas = {}
        for vertice in range(0,grafo.V()):
            self.aristas.update({vertice: []})
            self.distancias.append(self.INFINITE)
        self.calcular_minimo()


    def calcular_minimo(self):
        Q = []
        heapq.heapify(Q)
        heapq.heappush(Q, (heuristic(self.origen, self.destino), self.origen))
        self.distancias[self.origen] = 0
        self.padre[self.origen] = None
        priority, current = heapq.heappop(Q)
        while current != self.destino:
            vertices_adyacentes = self.grafo.adj(current)
            for vertice_adyacente in vertices_adyacentes:
                if not self.visitado(vertice_adyacente):
                    self.distancias[vertice_adyacente] = self.distancias[current] + 1
                    arista_adyacente = self.grafo.obtener_arista(current, vertice_adyacente)
                    self.aristas[vertice_adyacente] = list(self.aristas[current])
                    self.padre[vertice_adyacente] = current
                    if arista_adyacente:
                        self.aristas[vertice_adyacente].append(arista_adyacente)
                    heapq.heappush(Q, (heuristic(vertice_adyacente, self.destino), vertice_adyacente))
            priority, current = heapq.heappop(Q)


def heuristic(curr, dst):
    diff1 = locations[dst][0] - locations[curr][0]
    diff2 = locations[dst][1] - locations[curr][1]
    return sqrt((diff1**2) + (diff2**2))



graph = Digraph(9)
locations = [(0,0), (0,1), (0,2), (1,2), (1,0), (2,0), (2,1), (1,1), (2,2)]
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(0, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(0, 7)
graph.add_edge(6, 8)
graph.add_edge(3, 8)
graph.add_edge(7, 8)
search = bfs(graph, 0, 8)
print search.distancia(8)
print search.camino(8)