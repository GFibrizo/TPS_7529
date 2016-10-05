# -*- coding: latin-1 -*-
class Digraph:
    """Grafo no dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas. """

    def __init__(self, V):
        """Construye un grafo sin aristas de V vértices."""
        self.vertices = V
        self.aristas = {}
        for x in range(0, self.vertices):
            self.agregar(x)

    def V(self):
        """N�mero de v�rtices en el grafo.
           """
        return self.vertices

    def E(self):
       return len(self.iter_edges())

    def adj_e(self, v):
        """Itera sobre los aristas incidentes _desde_ v.
            """
        try:
            return self.aristas[v]
        except:
            print 'Vertice no valido'

    def adj(self, v):
        """Itera sobre los v�rtices adyacentes a ?v?.
           """
        try:
            vertices = []
            for arista in self.aristas[v]:
                vertices.append(arista.dst)
            return vertices
        except:
            print 'Vertice no valido'

    def add_edge(self, u, v, weight=0):
        """A�ade una arista al grafo.
           """
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
            self.aristas[u].append(Arista(u, v, weight))
        except:
            print 'Vertice no valido'

    def __iter__(self):
        """Itera de 0 a V."""
        return iter(range(self.get_vertices()))

    def iter_edges(self):
        aristas_totales = []
        for indice in self.aristas:
            for arista in self.aristas[indice]:
                aristas_totales.append(arista)
        return aristas_totales

    def agregar(self, nodo):
        self.aristas.update({nodo: []})


class Arista:
    """Arista de un grafo."""

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def src(self):
        return self.src

    def dst(self):
        return self.dst

    def weight(self):
        return self.weight


graph = Digraph(5)
graph.add_edge(3, 2, 5)
graph.add_edge(1, 3, 5)
graph.add_edge(3, 3, 5)
graph.add_edge(1, 4, 7)
graph.add_edge(2, 4, 7)
graph.add_edge(2, 4, 4)
graph.add_edge(2, 1, 7)
vertices = graph.adj(2)

print('Cantidad de aristas:' + str(graph.E()))
print('Cantidad de vertices:' + str(graph.V()))
print('Listado de vertices:' +str(graph.adj(1)))
print('Listado de aristas:' + str(graph.adj_e(2)))
print('Listado de aristas total:' + str(graph.iter_edges()))