INFINITE = 999999

class CaminoMinimo:
    def __init__(self, grafo, origen, destino):
        self.grafo = grafo
        self.origen = origen
        self.destino = destino
        self.INFINITE = INFINITE
        self.visitados = set()
        self.distancias = []
        self.recorrido = []
        self.padre = {}


    def distancia(self, v):
        return self.distancias[v]

    def camino(self, v):
        vertice = v
        recorrido = []
        while (vertice != None) and (self.padre[vertice] != None):
            recorrido.insert(0, self.grafo.obtener_arista(self.padre[vertice],vertice))
            vertice = self.padre[vertice]
        return recorrido

    def visitado(self, v):
        return v in self.visitados

    def _camino_minimo(self):
        pass