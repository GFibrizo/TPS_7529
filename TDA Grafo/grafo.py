# -*- coding: latin-1 -*-
class Digraph:
  """Grafo no dirigido con un número fijo de vértices.

  Los vértices son siempre números enteros no negativos. El primer vértice
  es 0.

  El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
  creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
  nuevas aristas.
  """
  def __init__(g, V):
    """Construye un grafo sin aristas de V vértices.
    """

  def V(g):
    """Número de vértices en el grafo.
    """
    pass

  def E(g):
    """Número de aristas en el grafo.
    """
    pass

  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    pass

  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    pass

  def add_edge(g, u, v, weight=0):
    """Añade una arista al grafo.
    """
    pass

  def __iter__(g):
    """Itera de 0 a V."""
    return iter(range(g.V()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.

    Las aristas devueltas tienen los siguientes atributos de solo lectura:

        e.src
        e.dst
        e.weight
    """
    pass

class Arista:
  """Arista de un grafo.
  """
  def __init__(self, src, dst, weight):
    pass


