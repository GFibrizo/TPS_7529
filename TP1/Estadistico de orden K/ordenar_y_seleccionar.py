def obtener_estadistico_orden_k(conjunto, k):

    conjunto_ordenado = sorted(conjunto)
    return conjunto_ordenado[k]

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
