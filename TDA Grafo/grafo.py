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
    self.node_count = V

  def get_vertices(self):
    """Número de vértices en el grafo.
    """
    return self.vertices

  def get_edges(self):
    """Número de aristas en el grafo."""
    pass

  def get_adjacent_edges_from(self, v):
    """Itera sobre los aristas incidentes _desde_ el vertice v."""
    pass

  def get_adjacent_edges_to(self, v):
    """Itera sobre los vértices adyacentes al vertice ‘v’."""
    pass

  def add_edge(self, u, v, weight=0):
    """Añade una arista al grafo. """
    pass

  def __iter__(self):
    """Itera de 0 a V."""
    return iter(range(self.get_vertices()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo."""
    pass

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
