def obtener_min_index(conjunto):
    minimo = min(conjunto)
    return conjunto.index(minimo)    

################################################################################

def obtener_estadistico_orden_k(conjunto, k):
    largo = len(conjunto)
    copia = conjunto[:]
    i = 0    
    while(True):
        indice_min = obtener_min_index(copia)
        copia[indice_min], copia[0] = copia[0], copia[indice_min]
        if (i >= k):
            break
        copia = copia[1:]
        i += 1
    return copia[0]

################################################################################
################################################################################

def test():
    print obtener_estadistico_orden_k([1], 0) == 1
    print obtener_estadistico_orden_k([2,1], 1) == 2
    print obtener_estadistico_orden_k([3,1,4,2,7], 3) == 4
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 0) == 1
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 7) == 8
    print obtener_estadistico_orden_k([1,2,3,4,5,6,7,8], 4) == 5

################################################################################
################################################################################

test()
