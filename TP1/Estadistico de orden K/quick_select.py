import heapq

def quick_select(conjunto, k):
    pivot = conjunto[0]
    menores = [x for x in conjunto if x < pivot]
    mayores = [x for x in conjunto if x > pivot]
    if k < len(menores):
        return quick_select(menores, k)
    elif k >= len(conjunto) - len(mayores):
        return quick_select(mayores, k - (len(conjunto) - len(mayores)))
    else:
        return pivot

################################################################################
################################################################################

def obtener_estadistico_orden_k(conjunto, k):
    return quick_select(conjunto, k)

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
