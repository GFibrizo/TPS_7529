def es_estadistico_orden_k(conjunto, candidato, k):

    largo = len(conjunto)
    copia = conjunto[:]
    i = 0    
    while(True):
        minimo = min(copia)
        indice_min = copia.index(minimo)
        copia[indice_min] = copia[0]
        copia[0] = minimo
        if (i >= k):
            break
        copia = copia[1:]
        i += 1

    print "Candidato: " + str(candidato) + "\tEstadistico de orden" + str(k) + ": " + str(copia[0])
    return candidato == copia[0]

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
