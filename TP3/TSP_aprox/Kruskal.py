import operator
import euler
from Arista import Arista
padre = dict()
ranking = dict()

def kruskal(graph):
    for vertice in graph.iter_vertexes():
        generar_set(vertice)
    mst = set()
    aristas = list(graph.iter_edges())
    aristas = sorted(aristas, key=operator.attrgetter('weight'))
    for arista in aristas:
        vertice1 = arista.src
        vertice2 = arista.dst
        if buscar_vertice(vertice1) != buscar_vertice(vertice2):
            union(vertice1, vertice2)
            mst.add(arista)
    return duplicar_camino(mst)

def duplicar_camino(mst):
    return_mst = set(mst)
    for arista in mst:
        nueva_arista = Arista(arista.dst, arista.src, arista.weight)
        return_mst.add(nueva_arista)
    return return_mst

def generar_set(vertice):
    padre[vertice] = vertice
    ranking[vertice] = 0

def union(vertice1, vertice2):
    raizA = buscar_vertice(vertice1)
    raizB = buscar_vertice(vertice2)
    if raizA != raizB:
        if ranking[raizA] > ranking[raizB]:
            padre[raizB] = raizA
        else:
            padre[raizA] = raizB
            if ranking[raizA] == ranking[raizB]: ranking[raizB] += 1

def buscar_vertice(vertice):
    if padre[vertice] != vertice:
        padre[vertice] = buscar_vertice(padre[vertice])
    return padre[vertice]

def encontrar_camino_de_euler(graph):
    mst = []
    i = 0
    for object in graph:
        obj = [object.src, object.dst, object.weight]
        mst.append(obj)
    camino_euler = euler.find_eulerian_tour(mst)
    camino_procesado, peso_total = procesar_euler(camino_euler, graph)
    return camino_procesado, peso_total

def obtener_arista(mst,src,dst):
    for arista in mst:
        if arista.src == src and arista.dst == dst:
            return arista

def eliminar_arista(mst, arista_a_eliminar):
    for arista in mst:
        if arista.src == arista_a_eliminar.src and arista.dst == arista_a_eliminar.dst:
            mst.remove(arista)
            return 1

def procesar_euler(camino, mst):
    retorno = []
    peso_total = 0
    anterior = None
    for vertice in camino:
        if anterior is None :
            anterior = vertice
            continue
        arista = obtener_arista(mst,anterior,vertice)
        retorno.append(arista)
        peso_total += arista.weight
        anterior = vertice
    return retorno, peso_total
