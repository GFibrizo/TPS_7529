from grafo import Digraph
from CaminoMinimo import CaminoMinimo
import heapq

class bfs(CaminoMinimo) :
    def __init__(self, grafo, origen, destino):
        CaminoMinimo.__init__(self,grafo,origen, destino)
        self.aristas = {}
        for vertice in range(0,grafo.V()):
            self.aristas.update({vertice: []})
            self.distancias.append(self.INFINITE)
        self.calcular_minimo()

    def calcular_minimo(self):
        Q = []
        Q.append(self.origen)
        self.distancias[self.origen] = 0
        self.padre[self.origen] = None
        current = Q.pop()
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
                    Q.append(vertice_adyacente)
            current = Q.pop()



graph = Digraph(5)
graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 4, 5)
graph.add_edge(2, 3, 5)
graph.add_edge(3, 4, 5)
bfs = bfs(graph,0,4)
print bfs.distancia(4)
print bfs.camino(4)
print "fin"