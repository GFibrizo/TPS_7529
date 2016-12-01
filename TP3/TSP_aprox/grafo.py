from Prim import Prim

class Digraph:

    def __init__(self, V):
        self.vertices = V
        self.aristas = {}
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
            self.aristas[u].append(Arista(u, v, weight))
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

    def agregar(self, nodo):
        self.aristas.update({nodo: []})

    def obtener_arista(self, origen, destino):
        aristas = self.adj_e(origen)
        for arista in aristas:
            if arista.dst == destino:
                return arista
        return None

    def obtener_tendido_minimo(self, archivo):
        graph = self.leer_matrix(archivo)
        prim = Prim()
        tendido_minimo = prim.calcular_tendido_minimo(graph)
        for arista in tendido_minimo:
            print arista

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
                    distances[current_vertex][vertex] = int(distance)
                current_vertex += 1
            return distances

class Arista:

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self._weight = weight

    def src(self):
        return self.src

    def dst(self):
        return self.dst

    def weight(self):
        return self._weight

    def __str__(self):
        return str(self.src)+"-->"+str(self.dst)

    def __repr__(self):
        return str(self.src) + "-->" + str(self.dst)


graph = Digraph(5)
graph.obtener_tendido_minimo('gr17_d.txt')

# print('Cantidad de aristas:' + str(graph.E()))
# print('Cantidad de vertices:' + str(graph.V()))
# print('Listado de vertices:' +str(graph.adj(1)))
# print('Listado de aristas:' + str(graph.adj_e(2)))
# print('Listado de aristas total:' + str(graph.iter_edges()))