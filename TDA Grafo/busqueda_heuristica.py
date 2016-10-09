from grafo import Digraph
from caminos import caminos
import heapq

class bfs(caminos) :
    def __init__(self, grafo, origen, destino):
        caminos.__init__(self,grafo,origen)
        self.destino = destino
        self.distancias = {}
        self.aristas = {}
        for vertice in range(0,grafo.V()):
            self.aristas.update({vertice: []})
            self.distancias.update({vertice: self.INFINITE})
        self.calcular_minimo()

    def heuristic(self, curr, dst):
        return dst - curr

    def calcular_minimo(self):
        Q = []
        heapq.heapify(Q)
        heapq.heappush(Q, (self.heuristic(self.origen, self.destino), self.origen))
        self.distancias[self.origen] = 0
        while len(Q) > 0:
            priority, current = heapq.heappop(Q)
            vertices_adyacentes = self.grafo.adj(current)
            for vertice_adyacente in vertices_adyacentes:
                if not self.visitado(vertice_adyacente):
                    self.distancias[vertice_adyacente] = self.distancias[current] + 1
                    arista_adyacente = self.grafo.obtener_arista(current, vertice_adyacente)
                    self.aristas[vertice_adyacente] = list(self.aristas[current])
                    if arista_adyacente:
                        self.aristas[vertice_adyacente].append(arista_adyacente)
                    heapq.heappush(Q, (self.heuristic(vertice_adyacente, self.destino), vertice_adyacente))

    def camino(self, v):
        try:
            return self.aristas[v]
        except:
            print "No se encontraron aristas para el vertice otorgado"
            return

    def distancia(self, v):
        try:
            return self.distancias[v]
        except:
            print "Distancia no calculada"
            return -1



graph = Digraph(5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
search = bfs(graph, 0, 4)
search.calcular_minimo() # Expected 3
print search.distancia(4) == 3

graph = Digraph(8)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(1, 4)
graph.add_edge(1, 2)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 7)
search = bfs(graph, 0, 7)
search.calcular_minimo()  # Expected 4
print search.distancia(7) == 4
