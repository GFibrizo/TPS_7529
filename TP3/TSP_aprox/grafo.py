from Prim import Prim
from Arista import Arista
import Kruskal

import time
import sys

import Kruskal

class Digraph:

    def __init__(self, V):
        self.vertices = V
        self.aristas = {}
        self.matrix = [[],[]]
        for x in range(0, self.vertices):
            self.agregar(x)

    def V(self):
        return self.vertices

    def E(self):
       return len(self.iter_edges())

    def adj_e(self, v):
        try:
            return self.aristas[v]
        except:
            print 'Vertice no valido'

    def adj(self, v):
        try:
            vertices = []
            for arista in self.aristas[v]:
                vertices.append(arista.dst)
            return vertices
        except:
            print 'Vertice no valido'

    def add_edge(self, u, v, weight=0):
        try:
            if v > self.V() - 1:
                print 'Vertice no valido'
                return
            aristas = self.aristas[u]
            for arista in aristas:
                if arista.dst == v:
                    ## si ya existe actualizo el peso
                    arista.weight = weight
                    return
            nueva_arista = Arista(u, v, weight)
            self.aristas[u].append(nueva_arista)
        except:
            print 'Vertice no valido'

    def __iter__(self):
        return iter(range(self.get_vertices()))

    def iter_edges(self):
        aristas_totales = []
        for indice in self.aristas:
            for arista in self.aristas[indice]:
                aristas_totales.append(arista)
        return aristas_totales

    def iter_vertexes(self):
        return list(range(0,self.V()))

    def agregar(self, nodo):
        self.aristas.update({nodo: []})

    def obtener_arista(self, origen, destino):
        aristas = self.adj_e(origen)
        for arista in aristas:
            if arista.dst == destino:
                return arista
        return None

    def obtener_tendido_minimo(self, archivo, inicial):
        graph = self.leer_matrix(archivo)
        prim = Prim()
        tendido_minimo = prim.calcular_tendido_minimo(graph, inicial)
        for arista in tendido_minimo:
            print arista

    def obtener_tendido_minimo_kruskal(self):
        tendido_minimo = Kruskal.kruskal(self)
        return Kruskal.encontrar_camino_de_euler(tendido_minimo)

    def obtener_matrix(self):
        graph = [[0] * self.vertices for _ in range(self.V())]
        for arista in self.iter_edges():
            graph[arista.src][arista.dst] = arista._weight
            graph[arista.dst][arista.src] = arista._weight
        return graph

    def leer_matrix(self, archivo):
        with open(archivo) as f:
            distances = {}
            current_vertex = 0
            for line in f:
                vertex_distances = line.rstrip("\n").split()
                distances[current_vertex] = {}
                for vertex, distance in enumerate(vertex_distances):
                    self.add_edge(current_vertex, vertex, int(distance))
                    distances[current_vertex][vertex] = int(distance)
                current_vertex += 1
            return distances

graph = Digraph(17)
archivo = sys.argv[1]
inicial = int(sys.argv[2])
time_start = time.time()
graph.leer_matrix(archivo)
camino_minimo, peso_total = graph.obtener_tendido_minimo_kruskal()
print "Total running time for file \"{}\" is {} seconds. El peso total calculado es: {}".format(archivo, time.time() - time_start, peso_total)