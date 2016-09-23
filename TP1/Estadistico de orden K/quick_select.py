import heapq


def es_estadistico_orden_k(conjunto, candidato, k):
    
    indice = conjunto.index(candidato)    
    menores = []    
#    mayores = []
    for elem in conjunto:
        if elem < candidato:
            menores.append(elem)
#        if elem > candidato:
#            mayores.append(elem)


    print "K: " + str(k) + "\tCant de menores: " + str(len(menores))
    return k == len(menores)

################################################################################
################################################################################

def test():
    print es_estadistico_orden_k([1], 1, 0)
    print es_estadistico_orden_k([2,1], 2, 1)
    print es_estadistico_orden_k([3,1,4,2,7], 4, 3)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 1, 0)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 8, 7)
    print es_estadistico_orden_k([1,2,3,4,5,6,7,8], 5, 4)

################################################################################
################################################################################

test()
