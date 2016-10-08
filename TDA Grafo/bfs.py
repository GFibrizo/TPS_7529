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

    def calcular_minimo(self):
        Q = []
        Q.append(self.origen)
        self.distancias[self.origen] = 0
        while len(Q) > 0:
            current = Q.pop()
            vertices_adyacentes = self.grafo.adj(current)
            for vertice_adyacente in vertices_adyacentes:
                if not self.visitado(vertice_adyacente):
                    self.distancias[vertice_adyacente] = self.distancias[current] + 1
                    arista_adyacente = self.grafo.obtener_arista(current, vertice_adyacente)
                    self.aristas[vertice_adyacente] = list(self.aristas[current])
                    if arista_adyacente:
                        self.aristas[vertice_adyacente].append(arista_adyacente)
                    Q.append(vertice_adyacente)

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
graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 4, 5)
graph.add_edge(3, 4, 5)
bfs = bfs(graph,0,4)
distancia = bfs.distancia(4)
aristas = bfs.camino(3)
print "fin"