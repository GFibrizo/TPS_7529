def es_estadistico_orden_k(conjunto, candidato, k):
    menores = 0
    for  elem in conjunto:
        if elem < candidato:       
            menores += 1
    return menores == k

################################################################################
################################################################################

def obtener_estadistico_orden_k(conjunto, k):
    for elemento in conjunto:
        if es_estadistico_orden_k(conjunto, elemento, k):
            return elemento
    return None        

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
