def es_estadistico_orden_k(conjunto, candidato, k):

    estadistico = []
    maximo = max(conjunto)
    for i in xrange(k+1):
        minimo_local = maximo        
        for elemento in conjunto:
            if (elemento not in estadistico) and (elemento < minimo_local):
                minimo_local = elemento
        estadistico.append(minimo_local)

    print "Candidato: " + str(candidato) + "\tEstadistico de orden" + str(k) + ": " + str(estadistico[k])
    return candidato == estadistico[k]

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
